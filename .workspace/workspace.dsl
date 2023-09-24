workspace "Blight of Yggdrasil" {

    model {
        player = person "Player"
        host = person "Host"

        gameSystem = softwareSystem "Blight of Yggdrasil" {
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
        systemContext gameSystem "SystemContext" {
            include *
            animation {
                gameSystem
                player
                host
            }
            autoLayout
            properties {
                structurizr.groups false
            }
        }

        container gameSystem "Containers" {
            include *
            animation {
                player host gameSystem
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