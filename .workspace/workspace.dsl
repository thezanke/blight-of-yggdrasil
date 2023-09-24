workspace "Blight of Yggdrasil" {

    model {
        player = person "Player"

        gameSystem = softwareSystem "Blight of Yggdrasil" {
            cliEntrypoint container "CLI Entrypoint" "Entrypoint to both the server and game client commands"
            clientApplication container "Game Client Application" "Allows the player to connect to a server and interact with the game"
            serv nt -> clientApplication
        cliEntrypoint -> serverApplication

        player -> clientApplication "Runs game client using"
        host -> serverApplication "Runs game client using"
    }

    views {
        systemContext softwareSystem "Diagram1" {
            include *
            autoLayout
        }

        styles {
            element "Software System" {
                background #1168bd
                color #ffffff
            }
            element "Person" {
                shape person
                background #08427b
                color #ffffff
            }
        }
    }

}