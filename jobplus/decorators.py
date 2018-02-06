from flask import abort
from flask_login import current_user
from functools import wraps
from jobplus.models import User

def role_required(role):
    """ 带参数的装饰器，可以使用它保护一个路由处理函数只能被待定的角色用户访问
    @role_required(User.ADMIN)
    def admin():
        pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwrargs):
            # 未登录用户或者角色不满足引发404
            if not current_user.is_authenticated or current_user.role < role:
                abort(404)
            return func(*args, **kwrargs)
        return wrapper
    return decorator

# 特定角色的装饰器
seeker_required = role_required(User.ROLE_SEEKER)
company_required = role_required(User.ROLE_COMPANY)
admin_required = role_required(User.ROLE_ADMIN)

