from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from rondo.extensions import db, bcrypt
from rondo.models.users import Users
from rondo.models.roles_permissions import Role, UserRoles, Permissions
from rondo.models.logs import Logs
from rondo.models.laptop import LaptopTable, laptopIventory

admin = Blueprint("admin", __name__)

@admin.route('/dashboard')
@login_required
def dashboard():
    return render_template("admin/main.html", title="Dashboard")

@admin.route('/inventory', methods=['GET', 'POST'])
@login_required
def inventory():
    if request.method == "POST":
        brand_name = request.form["brand-name"].strip()
        model_name = request.form["model-name"].strip()
        specs = request.form["specs"].strip()
        quantity = request.form["quantity"].strip()
        price = request.form["price"].strip()

        laptop_entry = LaptopTable(
            brand_name=brand_name, brand_model_name=model_name,brand_specifications=specs,
            quantity=int(quantity),price=int(price)
        )

        db.session.add(laptop_entry)
        db.session.commit()

        flash("Stock successfully added", "success")
        return redirect(url_for("admin.inventory"))


    
    return render_template("admin/inventory.html", title="Inventory")





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

#     return jsonify({"users": user.role.name})