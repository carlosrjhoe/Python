def make_album(name_artista, name_titulo):
    person_album = {'artista': name_artista.title(), 'titulo': name_titulo.title()}

    return person_album

if __name__ == "__main__":
    while True:
        print("\nPlease tell me a name artist:")
        print("(Enter 'Q' at any time to quit)")

        n_artist = input("Enter a artist: ").title()
        if n_artist == "Q":
            break

        a_artist = input("Enter a album the artist: ").title()
        if a_artist == "Q":
            break

        formatted_album = make_album(n_artist, a_artist)
        print(f"\n{formatted_album}")