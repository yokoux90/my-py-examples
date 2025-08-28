#pragma once

#include <drogon/HttpSimpleController.h>
#include <trantor/utils/Logger.h>

using namespace drogon;

class TestCtrl : public drogon::HttpSimpleController<TestCtrl>
{
public:
    void asyncHandleHttpRequest(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback) override;
    PATH_LIST_BEGIN
    PATH_ADD("/test", Get);
    PATH_LIST_END
};