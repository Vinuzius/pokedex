# Pokedex API Development Checklist

## 1. Pokémon Domain (`/pokemons`)
- [ X ] `GET /pokemons` - List Pokémon (Filters: `?status=`, `?name=`)
- [ X ] `GET /pokemons/{id}` - Get Pokémon details (include associated locations via join)
- [ X ] `PATCH /pokemons/{id}` - Update specific fields (e.g., capture status)


## 2. Games Domain (`/games`)
- [ X ] `GET /games` - List all games (Filters: `?generation=`)
- [ X ] `GET /games/{id}` - Get specific game details


## 3. Locations & Routes (`/locations`)
- [ X ] `GET /locations` - List locations (Filters: `?id_game=`)
- [ X ] `POST /locations` - Create a new route
- [ X ] `GET /locations/{id}/pokemons` - List all Pokémon that appear in a specific location


## 4. Encounters (`/encounters`)
- [ X ] `POST /encounters` - Link a Pokémon to a location (Payload: `id_pokemon`, `id_local`, `description`)
- [ X ] `DELETE /encounters/{id_pokemon}/{id_local}` - Remove a specific encounter association


## 5. Statistics (`/statistics`)
- [ X ] `GET /statistics/completion` - Return consolidated data (total Pokémon, count by status, overall completion %)

- [] - Get completion by generation