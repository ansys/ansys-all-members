import github
import os

# =============================================================================
#
# The purpose of this code is to connect to an org, extract its users and
# update the 'all-members' team of this org automatically with all the missing
# members.
#
# =============================================================================

# Insert your credentials... None by default
myPAT = None

# Select the org you want to access
myOrg = "ansys"

# =============================================================================
# MODIFY WITH CAUTION FROM THIS POINT ONWARDS
# =============================================================================

# Check if a value for PAT was provided
if myPAT is None:
    # This probably means that we are updating the team automatically using our
    # GitHub action: Nightly Team Update... let us read the GitHub Token
    myPAT = os.environ.get("token")

# Create a connection to GitHub
g = github.Github(myPAT)

# Let us get the org
gOrg = g.get_organization(myOrg)
print("Connecting to the " + gOrg.name + " organization...")

# Let us get the users
gOrg_members = gOrg.get_members()
print("Retrieving its members... Total count: " + str(gOrg_members.totalCount))

# Now, let us get the users of our all-members team
gAllMembersTeam = gOrg.get_team_by_slug("all-members")
gAllMembersTeam_members = gAllMembersTeam.get_members()
print(
    "Retrieving the 'all-members' team members... Total count: "
    + str(gAllMembersTeam_members.totalCount)
)

if gAllMembersTeam_members.totalCount != gOrg_members.totalCount:
    print("Users missing... let us check which ones!")

    # Let us check which are the missing members
    usersToAdd = []
    for gOrg_member in gOrg_members:
        # Check if the user is a member...
        if not gAllMembersTeam.has_in_members(gOrg_member):
            print(gOrg_member.login + " should be added!")
            usersToAdd.append(gOrg_member)

    # Show how many users will be added
    print("Users to be added: " + str(len(usersToAdd)))

    # Adding missing members to team
    for user in usersToAdd:
        gAllMembersTeam.add_to_members(user)
        print(user.login + " has been added!")
else:
    print("No users missing! All up-to-date.")
