#include "user_ctrl.h"

using namespace api::v1;

void UserCtrl::getInfo(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback, int userId) const
{
    Json::Value ret;
    ret["id"] = userId;
    ret["name"] = "cc-server-demo";
    auto resp = HttpResponse::newHttpJsonResponse(ret);
    callback(resp);
}

void UserCtrl::getDetailInfo(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback, int userId) const
{
    Json::Value ret;
    ret["id"] = userId;
    ret["name"] = "cc-server-demo";
    auto resp = HttpResponse::newHttpJsonResponse(ret);
    callback(resp);
}

void UserCtrl::newUser(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback, std::string &&userName)
{
    Json::Value ret;
    ret["id"] = 99;
    ret["name"] = userName;
    auto resp = HttpResponse::newHttpJsonResponse(ret);
    callback(resp);
}