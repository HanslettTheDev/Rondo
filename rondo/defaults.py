DEFAULT_ROLES = ["superadmin", "admin", "editor", "user"]

DEFAULT_PERMISSIONS = [
    "create",
    "read",
    "update",
    "delete",
    "assign_admin",
]

ROUTE_PATHS = {
    "superadmin": "superadmin.dashboard",
    "admin": "admin.dashboard",
    "editor": "editor.dashboard",
    "user": "user.dashboard",
}

DEFAULT_ROLE_PERMISSIONS = {
    "superadmin": [x for x in DEFAULT_PERMISSIONS],
    "admin": ["create", "read", "delete", "update"],
    "editor": ["update", "create"],
    "user": ["read", "pending"],
}

