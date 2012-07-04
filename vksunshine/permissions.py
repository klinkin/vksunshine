from flask.ext.principal import Permission, RoleNeed

# Create a permission with a single Need, in this case a RoleNeed.
admin = Permission(RoleNeed('admin'))
moderator = Permission(RoleNeed('moderator'))
auth = Permission(RoleNeed('authenticated'))

# this is assigned when you want to block a permission to all
# never assign this role to anyone !
null = Permission(RoleNeed='null')