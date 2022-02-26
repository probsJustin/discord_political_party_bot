import { BaseCommandInteraction, Client } from "discord.js";
import { Command } from "../Command";

export const VoteEdit: Command = {
    name: "vote_edit",
    description: "Returns a greeting",
    type: "CHAT_INPUT",
    run: async (client: Client, interaction: BaseCommandInteraction) => {
        const content = "vote_edit command run";

        await interaction.followUp({
            ephemeral: true,
            content
        });
    }
};