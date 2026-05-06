return {
  {
    "nvim-mini/mini.pairs",
    opts = {
      mappings = {
        -- Disable the double quote pair
        ['"'] = false,
        -- Keep the single quote pair (this is usually default, but explicit here for clarity)
        ["'"] = { action = "closeopen", pair = "''", neigh_pattern = "[^%a\\].", register = { cr = false } },
      },
    },
  },
}
