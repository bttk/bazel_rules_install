# Copyright 2018 The Bazel Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

workspace(name = "com_github_google_rules_install")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

local_repository(
    name = "com_github_google_rules_install_examples",
    path = "./examples",
)

local_repository(
    name = "com_github_google_rules_install_docs",
    path = "./docs",
)

load("@com_github_google_rules_install//:package.bzl", "install_rules_dependencies")

install_rules_dependencies()
