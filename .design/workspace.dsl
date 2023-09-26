workspace "Blight of Yggdrasil" {

    model {
        player = person "Player"
        host = person "Host"

        gameCliApplication = softwareSystem "Blight of Yggdrasil CLI Application" {
            cliEntrypoint = container "CLI Entrypoint" "Entrypoint to both the server and game client commands"
            clientApplication = container "Game Client Application" "Allows the player to connect to a server and interact with the game"
            serverApplication = container "Server Application" "Runs a server that allows players to connect and play the game"
        }

        cliEntrypoint -> clientApplication
        cliEntrypoint -> serverApplication

        player -> cliEntrypoint "Runs game client using"
        host -> cliEntrypoint "Runs game server using"
    }

    views {
        systemContext gameCliApplication "SystemContext" {
            include *
            animation {
                gameCliApplication
                player
                host
            }
            autoLayout
            properties {
                structurizr.groups false
            }
        }

        container gameCliApplication "Containers" {
            include *
            animation {
                player host gameCliApplication
                cliEntrypoint
                clientApplication
                serverApplication
            }
            autoLayout
        }

        styles {
            element "Software System" {
                background #1168bd
                color #ffffff
            }

            element "Container" {
                background #08427b
                color #ffffff
            }

            element "Person" {
                shape person
            }
        }
    }

}