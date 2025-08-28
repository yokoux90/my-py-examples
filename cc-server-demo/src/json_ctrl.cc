#include "json_ctrl.h"

void JsonCtrl::asyncHandleHttpRequest(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback)
{
    Json::Value ret;
    ret["app"] = "cc-server-demo";
    auto resp = HttpResponse::newHttpJsonResponse(ret);
    callback(resp);
}