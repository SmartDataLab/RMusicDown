#' <Add Title>
#'
#' <Add Description>
#'
#' @import htmlwidgets
#'
#' @export
music <- function(message, width = NULL, height = NULL, elementId = NULL) {

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