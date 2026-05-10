return {
  "vim-test/vim-test",
  dependencies = { "preservim/vimux" },
  keys = {
    { "<leader>tn", ":TestNearest<CR>", desc = "Nearest" },
    { "<leader>tf", ":TestFile<CR>", desc = "File" },
    { "<leader>ts", ":TestSuite<CR>", desc = "Suite" },
    { "<leader>tl", ":TestLast<CR>", desc = "Last" },
    { "<leader>tv", ":TestVisit<CR>", desc = "Visit" },
    { "<leader>th", ":VimuxCloseRunner<CR>", desc = "Hide Pane" },
    { "<leader>ti", ":VimuxInspectRunner<CR>", desc = "Inspect (Scroll)" },
  },
  config = function()
    vim.g["test#strategy"] = "vimux"
    vim.g["test#python#runner"] = "pytest"

    -- Ensure pytest uses 'uv run' if your env isn't automatically picked up
    -- vim.g["test#python#pytest#executable"] = "uv run pytest"

    vim.g.VimuxHeight = "30"
    vim.g.VimuxCloseOnExit = 0
  end,
}
