import { BaseCommandInteraction, Client } from "discord.js";
import { Command } from "../Command";

export const Debug: Command = {
    name: "debug",
    description: "Returns a greeting",
    type: "CHAT_INPUT",
    run: async (client: Client, interaction: BaseCommandInteraction) => {
        const content = "debug command run";

        await interaction.followUp({
            ephemeral: true,
            content
        });
    }
};