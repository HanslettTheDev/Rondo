from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from rondo.defaults import DEFAULT_ROLE_PERMISSIONS
from rondo.extensions import db, bcrypt
from rondo.models.users import Users
from rondo.models.roles_permissions import Role, Permissions
from rondo.models.logs import Logs
from rondo.models.laptop import LaptopTable, laptopIventory
from rondo.wrappers import role_required
from rondo.superadmin.utils import delete_previous_permissions, get_permission_objects, check_permission

superadmin = Blueprint("superadmin", __name__)

@superadmin.route('/dashboard')
@login_required
def dashboard():
    return render_template("superadmin/main.html", title="Dashboard")

@superadmin.route('/inventory', methods=['GET', 'POST'])
@login_required
@role_required(["superadmin", "admin"])
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
        return redirect(url_for("superadmin.inventory"))

    
    return render_template("superadmin/inventory.html", title="Inventory", laptops=laptops, cp=check_permission)

@superadmin.route("/inventory/edit/<int:id>", methods=["GET", "POST"])
@login_required
@role_required(["superadmin", "admin"])
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
        return redirect(url_for("superadmin.inventory"))
        
    return render_template("superadmin/edit_inventory.html", laptop=laptop[0])


@superadmin.route("/inventory/delete/<int:id>", methods=["GET", "POST"])
@login_required
@role_required(["superadmin", "admin"])
def delete_inventory(id):
    laptop = db.session.execute(db.select(LaptopTable).filter_by(id=id)).first()

    if laptop:
        db.session.delete(laptop[0])
        db.session.commit()

        flash("Record deleted successfully", "success")
        return redirect(url_for("superadmin.inventory"))
    else:
        flash("An error occured while deleting this record! Try again later", "danger")
        return redirect(url_for("superadmin.inventory"))


@superadmin.route('/user_management', methods=['GET', 'POST'])
@login_required
@role_required(["superadmin"])
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
        user = db.session.execute(db.select(Users).filter_by(username=users_account)).first()
        # Get the new role and assign it to the user
        role = db.session.execute(db.select(Role).filter_by(name=new_role)).first()
        # Check if the new role is the same as the old one
        if user[0].role.name.lower() == new_role:
            flash(f"Oops! Sorry! {user[0].username} already has this role!", "warning")
            return redirect(url_for("superadmin.user_management"))

        if not (user and role):
            flash('An unexpected error occured while assigning an admin', "info")
            return redirect(url_for("superadmin.user_management"))
        
        # Get all the permissions for that user
        user[0].role = role[0]

        # remove all permissions first
        for permission in user[0].permissions:
            delete_previous_permissions(user[0].id)

        for permission in get_permission_objects(new_permsisions):
            user[0].permissions.append(permission[0])

        db.session.commit()
        flash(
            f"<b>@{user[0].username}</b> has successfully been assigned the <b>{role[0].name}</b> role!", 
            "info"
        )
        return redirect(url_for('superadmin.user_management'))
    
    return render_template("superadmin/user_management.html", title="User Management", 
        users=users, roles=roles, permissions=permsisions
    )

@superadmin.route('/logs')
@login_required
@role_required(["superadmin"])
def logs():
    return render_template("superadmin/logs.html")
