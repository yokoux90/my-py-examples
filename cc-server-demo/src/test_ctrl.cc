#include "test_ctrl.h"

void TestCtrl::asyncHandleHttpRequest(
    const HttpRequestPtr &req,
    std::function<void(const HttpResponsePtr &)> &&callback)
{
    auto resp = HttpResponse::newHttpResponse();
    resp->setBody("<h1>cc-server-demo</h1>");
    resp->setExpiredTime(0);
    callback(resp);
}