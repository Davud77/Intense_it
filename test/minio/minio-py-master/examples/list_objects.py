# -*- coding: utf-8 -*-
# MinIO Python Library for Amazon S3 Compatible Cloud Storage,
# (C) 2015 MinIO, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from minio import Minio

client = Minio(
    "185.153.44.152:9001",
    access_key="YBPgiw5mGt4kyrJB",
    secret_key="LHIywTMipIkXYHLGn987lzfzel5Srtrr",
)

# List objects information.
objects = client.list_objects("my-bucket")
for obj in objects:
    print(obj)

# List objects information whose names starts with "my/prefix/".
objects = client.list_objects("my-bucket", prefix="my/prefix/")
for obj in objects:
    print(obj)

# List objects information recursively.
objects = client.list_objects("my-bucket", recursive=True)
for obj in objects:
    print(obj)

# List objects information recursively whose names starts with
# "my/prefix/".
objects = client.list_objects(
    "my-bucket", prefix="my/prefix/", recursive=True,
)
for obj in objects:
    print(obj)

# List objects information recursively after object name
# "my/prefix/world/1".
objects = client.list_objects(
    "my-bucket", recursive=True, start_after="my/prefix/world/1",
)
for obj in objects:
    print(obj)
