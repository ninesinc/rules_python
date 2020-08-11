load("@detectron2_test//:requirements.bzl", "requirement")
load("//python:defs.bzl", "py_library", "py_test")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # Apache 2.0

py_test(
    name = "detectron2_test",
    srcs = ["detectron2_test.py"],
    deps = [
        ":detectron2",
        ":torch",
    ],
)

py_library(
    name = "detectron2",
    deps = [
        requirement("cloudpickle"),
        requirement("cycler"),
        requirement("detectron2"),
        requirement("fvcore"),
        requirement("grpcio"),
        requirement("kiwisolver"),
        requirement("markdown"),
        requirement("matplotlib"),
        requirement("oauthlib"),
        requirement("portalocker"),
        requirement("pycocotools"),
        requirement("pydot"),
        requirement("pyparsing"),
        requirement("requests-oauthlib"),
        requirement("tabulate"),
        requirement("tensorboard"),
        requirement("tensorboard-plugin-wit"),
        requirement("torch"),
        requirement("werkzeug"),
        requirement("yacs"),
    ],
)

py_library(
    name = "torch",
    deps = [
        requirement("future"),
        requirement("numpy"),
        requirement("torch"),
    ],
)
