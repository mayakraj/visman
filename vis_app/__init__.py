

from app.main import app
from app.main import api
from app.main.routes.society import SocietyApi
from app.main.routes.user import UserApi
from app.main.routes.user import UserListApi
from app.main.routes.auth_controller import LoginAPI

from app.main.routes.society import society

app.register_blueprint(society)

api.add_resource(SocietyApi,'/society','/society/<int:soc_id>')
api.add_resource(UserListApi,'/user')
api.add_resource(UserApi,'/user/<int:public_id>')
api.add_resource(LoginAPI,'/auth/login')







