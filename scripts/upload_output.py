sl.u.AFmbN4SDzG3nGtPTPOcq8GoO8ZIsbfHKRP967tjWhTRuYfCdHknsw4emJLuzMlhgVLI19APA0uquqMb5jFHtkHpfwLzXbXwRgIB4sNCNVJM5P57Dr-u6JCpGkeZ1el-ViPRF-jnP6eOjJqa6HJWgY0EdyZ4LStn92TsoTzOnxeWHaAtZNV_BvmqoBDyOm1ftqQwr7m4KLApUEnePOAGTo9DV24NuDcRpe5Rf6xyKBswt727TJZsM614ILwdR6pqiOrIGLanPX5sJU3aafIU7ke3aZfkKeX1Ove4hEPpPXBkm-EHzdj4gvBSO8DsY6eiJJXLkEWlYAWlpEwjzXR4sByjjHwlOykrFmj2M_ZSCEPDkkFpveqRdqwogtOV9rs5NW3muv7yy6vb_QFbeVTqaD-edSbOBsSjRID6zas67QMQKTza_9s1qPiIbTGkmKC5UBuCqiBmcWQ2vcpOeK2fpQ0xC4VonxPTNgTx2eieueKqLITmrQdOhGNZpKPAnWxRYnQlAAPxOZhSypt8kk9tqDQKnWm0GyrqEX3bZXNkgUOx7Rc_1WoabOLi_sW9q5792ZEO_FFwB-dOAyTAqzesV9N3_h9de7Yzl5MZMCXBjxw7YJxFJqkFsQ189SAURBnR3otrQ-M3oUxEcVtJ_vrnNQk55ZdvFLmF4cpkBmMj7vlIW5_jw4nhVSVb5HOL4yYkuMKRHEazOVdbwN5KsEpfdy4qEM7GslDA3xNLQMpPShHa_iICFYtaMN0gmzSfZSTu8wVKUPUZy_V9UAQEPV3QrEHtxJSDO4b2vm-UXMgzWsnXFLRNzSgUqR1pv7HrBWSWAMNXOWvGJCt-cjeRe8DSnWRk_3ptXSYRWxrzoeUMn7laAms7IhE7FwWQKzfKvG9KhQ8vpO9Nku402rZVb-r2K2SGDOWDqKmeFSXnPnSA1SZvv02-sp5T56LbmgRDwmMPuo_O7Dhc-d7JGq34cu3fMEmexFniJa96PjnpZ7zU7YTf6a0iymcPD8gyqKSNoFGqHjhZWsMAXWoJipvqqkzxdm2Rf10ADEHqlgrJG5tdbKh6eTlChCFh9rOUdiPMo74XWZzOE8ssAnhqxlS2v8He41R0oYWHXuzvXshbT3TUVwNKtYKtAy6QORTzp4u5_ZjVtYzAOSNBGEfy-Zwh-RvHYVIg5yu2DmXbVe0G4TCS1S4r9r-MVRGE_RXHFHLuhp2K7_WfFDwcpROoOad4fQ9h2I_iZSKC_8_E8uA2vPqKI_wa4h2nojdRDNeuJmQJzTE4QDYQ5XV71R2SgGM3Z79N5l7Uusx0XqXX9Fm2kNjaQNZD09irRDtVv2Rpk43Z29pcP_7i2qQlp6ay4ESZeBrVyI_67MkJEZ9JfGXQTrx2-z8U4UVklaXkz1Sz1VX8oCCmBVhiTZyRgkFphn0y8LKFhDPd2Oh-jukHaHYD4dS34Dc4K1f7tMq55u1CTTr2Go8CoUo4

import dropbox
from dropbox.exceptions import ApiError

def upload_to_dropbox(file_path, dropbox_path, access_token):
    """
    将本地文件上传到Dropbox
    
    参数:
    file_path (str): 本地文件路径
    dropbox_path (str): Dropbox中的目标路径（包括文件名）
    access_token (str): Dropbox API访问令牌
    """
    try:
        # 创建Dropbox对象
        dbx = dropbox.Dropbox(access_token)
        
        # 读取本地文件
        with open(file_path, 'rb') as f:
            # 上传文件
            dbx.files_upload(f.read(), dropbox_path, mute=True)
            
        print(f"文件已成功上传到 Dropbox: {dropbox_path}")
        
    except ApiError as e:
        print(f"上传失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

# 使用示例
if __name__ == "__main__":
    # 替换为你的参数
    ACCESS_TOKEN = "sl.u.AFmbN4SDzG3nGtPTPOcq8GoO8ZIsbfHKRP967tjWhTRuYfCdHknsw4emJLuzMlhgVLI19APA0uquqMb5jFHtkHpfwLzXbXwRgIB4sNCNVJM5P57Dr-u6JCpGkeZ1el-ViPRF-jnP6eOjJqa6HJWgY0EdyZ4LStn92TsoTzOnxeWHaAtZNV_BvmqoBDyOm1ftqQwr7m4KLApUEnePOAGTo9DV24NuDcRpe5Rf6xyKBswt727TJZsM614ILwdR6pqiOrIGLanPX5sJU3aafIU7ke3aZfkKeX1Ove4hEPpPXBkm-EHzdj4gvBSO8DsY6eiJJXLkEWlYAWlpEwjzXR4sByjjHwlOykrFmj2M_ZSCEPDkkFpveqRdqwogtOV9rs5NW3muv7yy6vb_QFbeVTqaD-edSbOBsSjRID6zas67QMQKTza_9s1qPiIbTGkmKC5UBuCqiBmcWQ2vcpOeK2fpQ0xC4VonxPTNgTx2eieueKqLITmrQdOhGNZpKPAnWxRYnQlAAPxOZhSypt8kk9tqDQKnWm0GyrqEX3bZXNkgUOx7Rc_1WoabOLi_sW9q5792ZEO_FFwB-dOAyTAqzesV9N3_h9de7Yzl5MZMCXBjxw7YJxFJqkFsQ189SAURBnR3otrQ-M3oUxEcVtJ_vrnNQk55ZdvFLmF4cpkBmMj7vlIW5_jw4nhVSVb5HOL4yYkuMKRHEazOVdbwN5KsEpfdy4qEM7GslDA3xNLQMpPShHa_iICFYtaMN0gmzSfZSTu8wVKUPUZy_V9UAQEPV3QrEHtxJSDO4b2vm-UXMgzWsnXFLRNzSgUqR1pv7HrBWSWAMNXOWvGJCt-cjeRe8DSnWRk_3ptXSYRWxrzoeUMn7laAms7IhE7FwWQKzfKvG9KhQ8vpO9Nku402rZVb-r2K2SGDOWDqKmeFSXnPnSA1SZvv02-sp5T56LbmgRDwmMPuo_O7Dhc-d7JGq34cu3fMEmexFniJa96PjnpZ7zU7YTf6a0iymcPD8gyqKSNoFGqHjhZWsMAXWoJipvqqkzxdm2Rf10ADEHqlgrJG5tdbKh6eTlChCFh9rOUdiPMo74XWZzOE8ssAnhqxlS2v8He41R0oYWHXuzvXshbT3TUVwNKtYKtAy6QORTzp4u5_ZjVtYzAOSNBGEfy-Zwh-RvHYVIg5yu2DmXbVe0G4TCS1S4r9r-MVRGE_RXHFHLuhp2K7_WfFDwcpROoOad4fQ9h2I_iZSKC_8_E8uA2vPqKI_wa4h2nojdRDNeuJmQJzTE4QDYQ5XV71R2SgGM3Z79N5l7Uusx0XqXX9Fm2kNjaQNZD09irRDtVv2Rpk43Z29pcP_7i2qQlp6ay4ESZeBrVyI_67MkJEZ9JfGXQTrx2-z8U4UVklaXkz1Sz1VX8oCCmBVhiTZyRgkFphn0y8LKFhDPd2Oh-jukHaHYD4dS34Dc4K1f7tMq55u1CTTr2Go8CoUo4"  # 从Dropbox开发者页面获取
    LOCAL_FILE = "./test21.zip"  # 要上传的文件
    DROPBOX_PATH = "/ai_data/test21.zip"  # Dropbox中的路径
    
    upload_to_dropbox(LOCAL_FILE, DROPBOX_PATH, ACCESS_TOKEN)