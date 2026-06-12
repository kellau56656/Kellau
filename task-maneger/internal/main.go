package main

import (
	"net/http"
	"os"

	"task-manager/internal/handlers"
	"task-manager/internal/services"

	"github.com/urfave/cli/v2"
)

func main() {
	Run()
}

func Run() {
	authService := services.NewAuthService()
	authHandler := handlers.NewAuthHandler(authService)

	app := &cli.App{
		Name:  "myapp",
		Usage: "A simple CLI application",
		Action: func(c *cli.Context) error {
			println("Hello, World!")
			return nil
		},
	}

	if err := app.Run(os.Args); err != nil {
		println("Error:", err.Error())
		return
	}

	http.HandleFunc("/login", authHandler.LoginHandler)
	http.HandleFunc("/register", authHandler.RegisterHandler)
	http.HandleFunc("/logout", authHandler.LogoutHandler)

	println("Server listening on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		println("Server error:", err.Error())
	}
}
