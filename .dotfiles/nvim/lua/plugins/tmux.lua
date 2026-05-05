return {
  "christoomey/vim-tmux-navigator",
  lazy = false,
  cmd = {
    "TmuxNavigateLeft",
    "TmuxNavigateDown",
    "TmuxNavigateUp",
    "TmuxNavigateRight",
  },
  keys = {
    { "<C-h>", "<cmd>TmuxNavigateLeft<cr>", desc = "Window Left" },
    { "<C-j>", "<cmd>TmuxNavigateDown<cr>", desc = "Window Down" },
    { "<C-k>", "<cmd>TmuxNavigateUp<cr>", desc = "Window Up" },
    { "<C-l>", "<cmd>TmuxNavigateRight<cr>", desc = "Window Right" },
  },
}
