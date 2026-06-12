package services

import (
	"errors"
	"task-manager/internal/models"
)

type AuthService struct {
	users  map[string]models.User
	nextID int
}

func NewAuthService() *AuthService {
	s := &AuthService{
		users:  make(map[string]models.User),
		nextID: 1,
	}
	s.users["admin"] = models.User{
		ID:       1,
		Username: "admin",
		Password: "123",
	}
	return s
}

func (s *AuthService) Register(username, password string) (models.User, error) {
	if username == "" || password == "" {
		return models.User{}, errors.New("username and password required")
	}
	if _, ok := s.users[username]; ok {
		return models.User{}, errors.New("user already exists")
	}

	user := models.User{
		ID:       s.nextID,
		Username: username,
		Password: password,
	}

	s.users[username] = user
	s.nextID++

	return user, nil
}

func (s *AuthService) Login(username, password string) (models.User, error) {
	user, ok := s.users[username]
	if !ok || user.Password != password {
		return models.User{}, errors.New("invalid credentials")
	}
	return user, nil
}

func (s *AuthService) Logout(username string) error {
	if username == "" {
		return errors.New("username required")
	}
	if _, ok := s.users[username]; !ok {
		return errors.New("user not found")
	}
	return nil
}
