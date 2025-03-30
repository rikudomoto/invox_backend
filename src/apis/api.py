from flask_restful import Resource
import datetime

from flask import request
from flask import current_app as app
from src.apis.data.ai_analysis_log import AiAnalysisLogData
from src.models.ai_analysis_log import AiAnaLogModel
from src.apis.mock_api import MockAPI

class InvoxAPI(Resource):
  def post(self):
    """
    画像ファイルをAIに分析し結果をDBに登録するAPI

    Parameters
    -----------
    path:dict
      画像ファイルパス
    
    Returns
    -----------
    status_code, message:dict
    """
    request_parameter_dict = request.json
    app.logger.info("画像ファイルをAIに分析する処理開始 path: %s", request_parameter_dict)
    request_time=datetime.datetime.now()
    (ai_response, response_time) = MockAPI.mock_ai(request_parameter_dict["path"])
    app.logger.info("画像ファイルをAIに分析する処理終了 response: %s, response_time: %s", ai_response, response_time)
    
    app.logger.info("レスポンス情報を元にDBに登録処理開始")
    ai_analysis_log = AiAnalysisLogData()
    ai_analysis_log.image_path = request_parameter_dict["path"] or None
    ai_analysis_log.success = ai_response["success"]
    ai_analysis_log.message = ai_response["message"]
    ai_analysis_log.request_timestamp = request_time
    ai_analysis_log.response_timestamp = response_time
    if ai_response["success"]:
      # リクエストが成功した場合
      ai_analysis_log.class_label = ai_response["estimated_data"]["class"]
      ai_analysis_log.confidence = ai_response["estimated_data"]["confidence"]

    AiAnaLogModel.insert(ai_analysis_log)
    app.logger.info("レスポンス情報を元にDBに登録処理終了")

    return {"status": 200, "message": ai_response["message"]}
