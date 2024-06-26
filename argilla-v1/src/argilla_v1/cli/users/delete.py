#  Copyright 2021-present, the Recognai S.L. team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import TYPE_CHECKING

import typer

if TYPE_CHECKING:
    from argilla_v1.client.users import User


def delete_user(ctx: typer.Context) -> None:
    from argilla_v1.cli.rich import echo_in_panel

    user: "User" = ctx.obj

    try:
        user.delete()
    except RuntimeError as e:
        echo_in_panel(
            "An unexpected error occurred when trying to remove the user.",
            title="Unexpected error",
            title_align="left",
            success=False,
        )
        raise typer.Exit(code=1) from e

    echo_in_panel(f"User with username={user.username} has been removed.", title="User removed", title_align="left")
