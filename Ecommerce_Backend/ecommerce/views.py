from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .controllers import RegisterUserController
from .controllers import RegisterProductController
from .controllers import UpdateProductController
from .controllers import ViewProductsController
from .controllers import AuthUserController
from .controllers import OrderProductsController
from .controllers import MyOrdersController
from .controllers import UpdateOrderStatusController
import traceback

def makeCallback(controller,mtd):
    @api_view([mtd])
    def callback(req,**params):
        try:
            header=dict()
            if("HTTP_AUTHORIZATION" in req.META):
                header["Authorization"]=req.META["HTTP_AUTHORIZATION"]
            http_req={"header":header,
            "body":req.data,
            "query":req.query_params,
            "params":params,
            "method":req.method,
            "path":req.path}
            return Response(controller(http_req))
        except Exception as e:
            print(e)
            traceback.print_exc()

            return Response("Internal Server Failure")

    return callback  

userView= makeCallback(RegisterUserController.registerUser,'POST')    
productView= makeCallback(RegisterProductController.registerProduct,'POST')    
authView= makeCallback(AuthUserController.fetchToken,'POST')    
authOTPView =makeCallback(AuthUserController.fetchToken,'POST') 
updateProductView= makeCallback(UpdateProductController.updateProduct,'PATCH')   
showAllProductsView =  makeCallback(ViewProductsController.viewAllProduct,'GET')   
showAProductView =  makeCallback(ViewProductsController.viewAProduct,'GET')   
orderProductView =  makeCallback(OrderProductsController.orderProduct,'POST')   
myOrdersView = makeCallback(MyOrdersController.viewAllOrders,'GET')
updateOrderStatusView = makeCallback(UpdateOrderStatusController.updateStatus,'PATCH')   



