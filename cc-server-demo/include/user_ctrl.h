#pragma once

#include <drogon/HttpController.h>
#include <trantor/utils/Logger.h>

using namespace drogon;

namespace api
{
    namespace v1
    {
        class UserCtrl : public drogon::HttpController<UserCtrl>
        {
        public:
            METHOD_LIST_BEGIN
            // Drogon automatically appends the namespace and name of the controller to
            // the handlers of the controller. In this example, although we are adding
            // a handler to /. But because it is a part of the SayHello controller. It
            // ends up in path /SayHello/ (IMPORTANT! It is /SayHello/ not /SayHello
            // as they are different paths).

            // /api/v1/UserCtrl/12
            METHOD_ADD(UserCtrl::getInfo, "/{id}", Get);
            // /api/v1/UserCtrl/12/detail
            METHOD_ADD(UserCtrl::getDetailInfo, "/{id}/detail", Get);
            // // /api/v1/UserCtrl/John
            METHOD_ADD(UserCtrl::newUser, "/{name}", Post);
            METHOD_LIST_END

            void getInfo(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback, int userId) const;
            void getDetailInfo(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback, int userId) const;
            void newUser(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback, std::string &&userName);

        public:
            UserCtrl()
            {
                LOG_DEBUG << "User Controller Constructor";
            }
        };
    }
}
