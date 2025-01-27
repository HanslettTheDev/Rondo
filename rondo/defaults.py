DEFAULT_ROLES = ["superadmin", "admin", "editor", "user"]

DEFAULT_PERMISSIONS = [
    "create", "read", "update", "delete", "view",
    "superadmin.create_admin", 
]

DEFAULT_ROLE_PERMISSIONS = {
    "superadmin": ["all"],
    "admin": ["create", "read", "delete", "update"],
    "editor": ["view", "create"],
    "user": ["view"]
}