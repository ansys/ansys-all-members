# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Script for automatically updating the ansys/all-members GitHub team
from the Ansys Organization. This team basically includes all members
within the organization."""

import os

import github

# =============================================================================
#
# The purpose of this code is to connect to an org, extract its users and
# update the 'all-members' team of this org automatically with all the missing
# members.
#
# =============================================================================

# Insert your credentials... None by default
MY_PAT = None

# Select the org you want to access
MY_ORG = "ansys"

# =============================================================================
# MODIFY WITH CAUTION FROM THIS POINT ONWARDS
# =============================================================================

# Check if a value for PAT was provided
if MY_PAT is None:
    # This probably means that we are updating the team automatically using our
    # GitHub action: Team Update... let us read the GitHub Token
    print("Reading access token from 'TOKEN' environment variable...")
    MY_PAT = os.environ.get("TOKEN", default=None)

# If the value for PAT is still None... throw error!
if MY_PAT is None:
    raise ValueError("No PAT value available. Consider adding it.")

# Create a connection to GitHub
g = github.Github(MY_PAT)

# Let us get the org
g_org = g.get_organization(MY_ORG)
print(f"Connecting to the {g_org.name} organization...")

# Let us get the users
g_org_members = g_org.get_members()
print(f"Retrieving members... Total count: {g_org_members.totalCount}")

# Now, let us get the users of our all-members team
g_team = g_org.get_team_by_slug("all-members")
g_team_members = g_team.get_members()
print(
    "Retrieving the 'all-members' team members... "
    + f"Total count: {g_team_members.totalCount}"
)

# In case there are missing members... let us add them!
if g_team_members.totalCount != g_org_members.totalCount:
    print("Users missing... let us check which ones!")

    # Store the difference
    diff = g_org_members.totalCount - g_team_members.totalCount

    # Let us check which are the missing members
    users_to_add = set()
    for g_org_member in g_org_members:
        # Check if the user is a member...
        if not g_team.has_in_members(g_org_member):
            print(f"{g_org_member.login} should be added!")
            users_to_add.add(g_org_member)

        # Check if we have identified all missing users
        if diff == len(users_to_add):
            break

    # Show how many users will be added
    print(f"Users to be added: {len(users_to_add)}")

    # Adding missing members to team
    for user in users_to_add:
        try:
            g_team.add_to_members(user)
            print(f"{user.login} has been added!")
        except github.GithubException as e:
            print(f"Error adding {user.login}: {e}")

else:
    print("No users missing! All up-to-date.")
