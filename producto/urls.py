from rest_framework import routers
from .api import ProductoViewSet, TipoViewSet, MesaViewSet, ClienteViewSet, ProveedorViewSet, EmpleadosViewSet        

router=  routers.DefaultRouter()

router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/tipo', TipoViewSet, 'tipo')
router.register('api/mesa', MesaViewSet, 'mesa')
router.register('api/cliente', ClienteViewSet, 'cliente')
router.register('api/proveedor', ProveedorViewSet, 'proveedor')
router.register('api/empleados', EmpleadosViewSet, 'empleados')
urlpatterns = router.urls
