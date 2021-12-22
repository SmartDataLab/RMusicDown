#' <Add Title>
#'
#' <Add Description>
#'
#' @import htmlwidgets
#'
#' @export
now_playing_music <- function(message, width = NULL, height = NULL, elementId = NULL) {

  # forward options using x
  x <- list(
    message = message
  )

  # create widget
  htmlwidgets::createWidget(
    name = "mywidget",
    x,
    width = width,
    height = height,
    package = "mywidget",
    elementId = elementId
  )
}

#' @export
netease_music <- function(query = "代码", show_in_viewer = TRUE, select = 1) {
  # do some thing
  if (.Platform$OS.type == "unix") {
    mac_address <- system("cat /sys/class/net/*/address", intern = TRUE)
  } else {
    mac_address <- system("getmac", intern = TRUE)
  }
  url <- URLencode(paste("http://smartdata.ruc.edu.cn/rmusicdown/search?query=", query, "&mac_address=", mac_address, "&choice=", select, sep = ""), repeated = FALSE)
  x <- httr::GET(url)
  res <- httr::content(x, as = "parsed")
  print("default select 1, there are 20 playlists. use select param to select new one. If there is no content in the player for a selected playlist, maybe the playlist contains vip songs.")
  print("select No. | id | name | play count")
  for (i in 1:length(res$result$playlists)) {
    id <- res$result$playlists[[i]]$id
    name <- res$result$playlists[[i]]$name
    playcount <- res$result$playlists[[i]]$playCount
    print(paste(i, id, name, playcount, sep = " | "))
  }
  if (select >= 1 && select <= length(res$result$playlists)) {
    id <- res$result$playlists[[select]]$id
  } else {
    id <- "4886213342"
  }
  # some request
  view_url <- paste("http://music.163.com/outchain/player?type=0&id=", id, "&auto=1&height=430", sep = "")
  if (show_in_viewer) {
    rstudioapi::viewer(view_url)
  }
  knitr::include_url(view_url)
}


#' Shiny bindings for mywidget
#'
#' Output and render functions for using mywidget within Shiny
#' applications and interactive Rmd documents.
#'
#' @param outputId output variable to read from
#' @param width,height Must be a valid CSS unit (like \code{'100\%'},
#'   \code{'400px'}, \code{'auto'}) or a number, which will be coerced to a
#'   string and have \code{'px'} appended.
#' @param expr An expression that generates a mywidget
#' @param env The environment in which to evaluate \code{expr}.
#' @param quoted Is \code{expr} a quoted expression (with \code{quote()})? This
#'   is useful if you want to save an expression in a variable.
#'
#' @name music-shiny
#'
#' @export
musicOutput <- function(outputId, width = "100%", height = "400px") {
  htmlwidgets::shinyWidgetOutput(outputId, "mywidget", width, height, package = "mywidget")
}

#' @rdname music-shiny
#' @export
renderMusic <- function(expr, env = parent.frame(), quoted = FALSE) {
  if (!quoted) {
    expr <- substitute(expr)
  } # force quoted
  htmlwidgets::shinyRenderWidget(expr, musicOutput, env, quoted = TRUE)
}