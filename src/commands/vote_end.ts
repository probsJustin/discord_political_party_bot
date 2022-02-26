import { BaseCommandInteraction, Client } from "discord.js";
import { Command } from "../Command";

export const VoteEnd: Command = {
    name: "vote_end",
    description: "Returns a greeting",
    type: "CHAT_INPUT",
    run: async (client: Client, interaction: BaseCommandInteraction) => {
        const content = "vote_end command run";

        await interaction.followUp({
            ephemeral: true,
            content
        });
    }
};