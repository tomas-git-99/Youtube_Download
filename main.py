import frond
import back
from multiprocessing import  freeze_support

if __name__ ==  '__main__':
    freeze_support()
    backend_obj = back.Download_completo()
    frontend_obj = frond.Perro()
    frontend_obj.run()