import datetime
from flask import current_app as app

class MockAPI():
  def mock_ai(path):
    """
    AI分析モックAPI
    ・pathに値が存在すれば成功
    ・pathに値が存在しなければ失敗
    
    Parameters
    -----------
    path:string
      画像ファイルパス
    
    Returns
    -----------
    response:dict
    datetime.datetime.now()
    """

    if path:
      app.logger.info("リクエスト成功")
      response = {
        "success": True,
        "message": "success",
        "estimated_data": {
          "class": 3,
          "confidence": 0.8683
        }
      }
      return response, datetime.datetime.now()
    else:
      app.logger.error("リクエスト失敗")
      response = {
        "success": False,
        "message": "Error:E50012",
        "estimated_data": {}
      }
      return response, datetime.datetime.now()