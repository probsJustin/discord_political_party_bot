import { BaseCommandInteraction, Client } from "discord.js";
import { Command } from "../Command";

export const VoteStart: Command = {
    name: "vote_start",
    description: "Returns a greeting",
    type: "CHAT_INPUT",
    run: async (client: Client, interaction: BaseCommandInteraction) => {
        const content = "vote_start command run";

        await interaction.followUp({
            ephemeral: true,
            content
        });
    }
};