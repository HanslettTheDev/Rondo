from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from rondo.admin.utils import get_permission_objects
from rondo.defaults import DEFAULT_ROLE_PERMISSIONS
from rondo.extensions import db, bcrypt
from rondo.models.users import Users
from rondo.models.roles_permissions import Role, UserRoles, Permissions
from rondo.models.logs import Logs
from rondo.models.laptop import LaptopTable, laptopIventory
from rondo.wrappers import role_required

admin = Blueprint("admin", __name__)

@admin.route('/dashboard')
@login_required
def dashboard():
    return render_template("admin/main.html", title="Dashboard")

@admin.route('/inventory', methods=['GET', 'POST'])
@login_required
def inventory():
    laptops = db.session.execute(db.select(LaptopTable)).all()
    
    if request.method == "POST":
        brand_name = request.form["brand-name"].strip()
        model_name = request.form["model-name"].strip()
        specs = request.form["specs"].strip()
        quantity = request.form["quantity"].strip()
        price = request.form["price"].strip()
        price = int(price) if price != "" else ""

        laptop_entry = LaptopTable(
            brand_name=brand_name, brand_model_name=model_name,brand_specifications=specs,
            quantity=int(quantity),price=price
        )

        db.session.add(laptop_entry)
        db.session.commit()

        flash("Stock successfully added", "success")
        return redirect(url_for("admin.inventory"))

    
    return render_template("admin/inventory.html", title="Inventory", laptops=laptops)

@admin.route("/inventory/edit/<int:id>", methods=["GET", "POST"])
def edit_inventory(id):
    laptop = db.session.execute(db.select(LaptopTable).filter_by(id=id)).first()

    if request.method == "POST":
        laptop[0].brand_name = request.form["brand-name"].strip()
        laptop[0].brand_model_name = request.form["model-name"].strip()
        laptop[0].brand_specifications = request.form["specs"].strip()
        laptop[0].quantity = request.form["quantity"].strip()
        price = request.form["price"].strip()
        laptop[0].price = int(price) if price != "" else ""

        db.session.add(laptop[0])
        db.session.commit()

        flash("Record Modified Successfully", "success")
        return redirect(url_for("admin.inventory"))
        
    return render_template("admin/edit_inventory.html", laptop=laptop[0])


@admin.route("/inventory/delete/<int:id>", methods=["GET", "POST"])
def delete_inventory(id):
    laptop = db.session.execute(db.select(LaptopTable).filter_by(id=id)).first()

    if laptop:
        db.session.delete(laptop[0])
        db.session.commit()

        flash("Record deleted successfully", "success")
        return redirect(url_for("admin.inventory"))
    else:
        flash("An error occured while deleting this record! Try again later", "danger")
        return redirect(url_for("admin.inventory"))


@admin.route('/user_management', methods=['GET', 'POST'])
@login_required
def user_management():
    users = db.session.execute(db.select(Users)).all()
    roles = db.session.execute(db.select(Role)).all()
    permsisions = db.session.execute(db.select(Permissions)).all()

    if request.method == "POST":
        users_account = request.form["users-account"].strip()
        new_role = request.form["users-role"].strip().lower()
        new_permsisions = (
            request.form["custom-permissions"].strip().split(" ") if 
            request.form["is-default"].lower() == "no" 
            else DEFAULT_ROLE_PERMISSIONS[new_role]
        )
        print(new_permsisions)

        user = db.session.execute(db.select(Users).filter_by(username=users_account)).first()
        # Get the new role and assign it to the user
        role = db.session.execute(db.select(Role).filter_by(name=new_role)).first()
        # Check if the new role is the same as the old one
        if user[0].role.name.lower() == new_role:
            flash(f"Oops! Sorry! {user[0].username} already has this role!", "warning")
            return redirect(url_for("admin.user_management"))
        # TODO: Fix the small bug where the permission id needs to removed from the user_permissions table
        # before being added as the new Permissions
        # That is the users permissions should be removed completely and then the new ones assigned to the user

        if user and role:
            user[0].role = role[0]
            for permission in get_permission_objects(new_permsisions):
                user[0].permissions.append(permission[0])

        db.session.commit()
        flash(
            f"<b>@{user[0].username}</b> has successfully been assigned the <b>{role[0].name}</b> role!", 
            "info"
        )
        return redirect(url_for('admin.user_management'))
    
    return render_template("admin/user_management.html", title="User Management", 
        users=users, roles=roles, permissions=permsisions
    )


# @admin.route("/fill")
# def fill():
#     role = Role()
#     role.add_default_roles()

#     permission = Permissions()
#     permission.add_default_permissions()

#     roles = Role.query.all()
#     permissions = Permissions.query.all()


#     return jsonify({"role": list([role.name for role in roles]), "permission": list([permission.name for permission in permissions])})

# @admin.route("/test", methods=["GET", "POST"])
# def register():
#     # user = Users(
#     #     username="admin", name="tambe hanslett", 
#     #     email="admin", password=bcrypt.generate_password_hash("admin")
#     # )

#     user = Users.query.filter_by(username="admin").first()

#     # user.role = Role.query.filter_by(name="superadmin").first()
#     # Give this user 3 more permissions 
#     perm1 = Permissions.query.filter_by(name="superadmin.create_admin").first()
#     perm2 = Permissions.query.filter_by(name="create").first()
#     perm3 = Permissions.query.filter_by(name="read").first()

#     user.permissions.append(perm1)
#     user.permissions.append(perm2)
#     user.permissions.append(perm3)
#     # db.session.add(user)
#     db.session.commit()

#     return jsonify({"users":  user.role.name})
