import { BaseCommandInteraction, Client } from "discord.js";
import { Command } from "../Command";

export const Vote: Command = {
    name: "vote",
    description: "Returns a greeting",
    type: "CHAT_INPUT",
    run: async (client: Client, interaction: BaseCommandInteraction) => {
        const content = " Hey, you voted!";

        await interaction.followUp({
            ephemeral: true,
            content
        });
    }
};