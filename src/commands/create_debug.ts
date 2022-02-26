import { BaseCommandInteraction, Client } from "discord.js";
import { Command } from "../Command";

export const Create: Command = {
    name: "create",
    description: "Returns a greeting",
    type: "CHAT_INPUT",
    run: async (client: Client, interaction: BaseCommandInteraction) => {
        const content = "create command run";

        await interaction.followUp({
            ephemeral: true,
            content
        });
    }
};