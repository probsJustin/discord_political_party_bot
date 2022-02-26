import { Command } from "./Command";
import { Hello } from "./commands/hello";
import { Vote } from "./commands/vote";
import { Debug } from "./commands/debug";
import { Create } from "./commands/create_debug";
import { VoteEdit } from "./commands/vote_edit";
import { VoteEnd } from "./commands/vote_end";
import { VoteStart } from "./commands/vote_start";
import { Ping } from "./commands/ping";

export const Commands: Command[] = [
Hello,
Vote,
Debug,
Create,
VoteEdit,
VoteEnd,
VoteStart,
Ping
];