#include <drogon/drogon.h>
#include <trantor/utils/Logger.h>
#include <filesystem>

#ifdef _WIN32
#include <WS2tcpip.h>
#else
#include <netinet/tcp.h>
#include <sys/socket.h>
#endif

#include "test_ctrl.h"
#include "json_ctrl.h"
#include "user_ctrl.h"

using namespace drogon;
namespace fs = std::filesystem;

int main()
{
    fs::path log_folder = "./log";

    if (fs::create_directory(log_folder))
    {
        LOG_INFO << "Log folder has been created successfully.";
    }

    LOG_INFO << "Server running on http://127.0.0.1:8088";
    app()
        .setLogPath(log_folder.string())
        .setLogLevel(trantor::Logger::kTrace)
        // .loadConfigFile("./config.json")
        .setThreadNum(6);

    app()
        .setBeforeListenSockOptCallback([](int fd)
                                        {
                                            LOG_INFO << "setBeforeListenSockOptCallback:" << fd;
#ifdef _WIN32
#elif __linux__
                                            int enable = 1;
                                            if (setsockopt(
                                                    fd, IPPROTO_TCP, TCP_FASTOPEN, &enable, sizeof(enable)) ==
                                                -1)
                                            {
                                                LOG_INFO << "setsockopt TCP_FASTOPEN failed";
                                            }
#else
#endif
                                        })
        .setAfterAcceptSockOptCallback([](int) {});

#ifdef _WIN32
#elif __linux__
    app().enableRunAsDaemon();
#else
#endif

    app().addListener("0.0.0.0", 8088).run();
    return 0;
}