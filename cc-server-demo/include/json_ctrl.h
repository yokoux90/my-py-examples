#pragma once

#include <drogon/HttpSimpleController.h>
#include <trantor/utils/Logger.h>

using namespace drogon;

class JsonCtrl : public drogon::HttpSimpleController<JsonCtrl>
{
public:
    void asyncHandleHttpRequest(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback) override;
    PATH_LIST_BEGIN
    PATH_ADD("/json", Get);
    PATH_LIST_END
};