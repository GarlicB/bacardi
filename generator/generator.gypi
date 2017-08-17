# Copyright (c) 2017 The Lunch Class Authors.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'targets': [
    {
      'target_name': 'generator',
      'type': 'none',
      'actions': [
        {
          'action_name': 'tsc',
          'inputs': [
            'main.ts',
          ],
          'outputs': [
            '<@(PRODUCT_DIR)/generator'
          ],
          'action': [
            '<@(PRODUCT_DIR)/../../bootstrap/command/tsc',
            '<@(_inputs)',
            '--outDir',
            '<@(_outputs)',
          ],
        },
      ],
    },
  ],
}
