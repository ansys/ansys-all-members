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
my_pat = None

# Select the org you want to access
my_org = "pyansys"

# =============================================================================
# MODIFY WITH CAUTION FROM THIS POINT ONWARDS
# =============================================================================

# Check if a value for PAT was provided
if my_pat is None:
    # This probably means that we are updating the team automatically using our
    # GitHub action: Team Update... let us read the GitHub Token
    print("Reading access token from 'TOKEN' environment variable...")
    my_pat = os.environ.get("TOKEN")

# Create a connection to GitHub
g = github.Github(my_pat)

# Let us get the org
g_org = g.get_organization(my_org)
print("Connecting to the " + g_org.name + " organization...")

# Let us get the users
g_org_members = g_org.get_members()
print("Retrieving members... Total count: " + str(g_org_members.totalCount))

# Now, let us get the users of our all-members team
g_team = g_org.get_team_by_slug("all-members")
g_team_members = g_team.get_members()
print(
    "Retrieving the 'all-members' team members... Total count: "
    + str(g_team_members.totalCount)
)

if g_team_members.totalCount != g_org_members.totalCount:
    print("Users missing... let us check which ones!")

    # Store the difference
    diff = g_org_members.totalCount - g_team_members.totalCount

    # Let us check which are the missing members
    users_to_add = []
    for g_org_member in g_org_members:
        # Check if the user is a member...
        if not g_team.has_in_members(g_org_member):
            print(g_org_member.login + " should be added!")
            users_to_add.append(g_org_member)

        # Check if we have identified all missing users
        if diff == len(users_to_add):
            break

    # Show how many users will be added
    print("Users to be added: " + str(len(users_to_add)))

    # Adding missing members to team
    for user in users_to_add:
        g_team.add_to_members(user)
        print(user.login + " has been added!")
else:
    print("No users missing! All up-to-date.")
