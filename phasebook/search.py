from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database"""
    if(not args):
        return USERS
    filtered_users = []
    for key, value in args.items():
        for user in USERS:
            if(user[key] == value or 
                (key == 'age' and (user[key] == int(value) or user[key] == int(value) - 1 or user[key] == int(value) + 1)) or 
                ((key == 'name' or key == 'occupation') and value.lower() in user[key].lower())):
                if not any(userid.get('id','') == user['id'] for userid in filtered_users):
                    filtered_users.append(user)
    return filtered_users

