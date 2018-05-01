from flask import jsonify
import re
from eventmanager.helpers.helpers import to_json
from flask.views import MethodView
from . import user
from eventmanager.models import User


class UserApi(MethodView):

  def get(self, user_id=None):

    if user_id is None:
      users = [to_json(**vars(user)) for user in User.query.all()]
      return jsonify(dict(users=users))

    user = to_json(**vars(User.query.get(user_id))) if User.query.get(user_id) else {}

    if user:
      return jsonify(dict(user=user))

    return jsonify(dict(user=user)), 404


user.add_url_rule('/', view_func=UserApi.as_view('user'))
user.add_url_rule('/<int:user_id>', view_func=UserApi.as_view('users'))

