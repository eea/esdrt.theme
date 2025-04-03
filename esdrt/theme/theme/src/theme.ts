import * as moment from "moment";

function hightlight_restructured() {
  const elBody = $("body");
  if (
    elBody.hasClass("template-esdrt-content-observation") ||
    elBody.hasClass("template-esdrt-content-conclusion") ||
    elBody.hasClass("template-edit-highlights") ||
    elBody.hasClass("template-edit portaltype-conclusion") ||
    elBody.hasClass("template-esdrt-content-conclusion") ||
    elBody.hasClass("template-esdrt-content-conclusionsphase2") ||
    elBody.hasClass("template-edit portaltype-conclusionsphase2") ||
    elBody.hasClass("template-view portaltype-observation")
  ) {
    $(
      "<br/><br/><span style='font-weight:bold'>Draft/final conclusion flags</span><br/>"
    ).insertBefore($("input[value='psi']").parent());
  }
}

$(function () {
  $(".collapsiblePanelTitle").on("click", function (e) {
    var panel = $(this).data("panel");
    if ($(this).hasClass("collapsed")) {
      $("." + panel).show();
      if (panel == "observation-workflow") {
        $("#workflowTable")
          .parent()
          .scrollLeft($("#workflowTable").outerWidth());
      }
    } else {
      $("." + panel).hide();
    }
    $(this).toggleClass("collapsed");
  });
  $(".collapsibleListTitle").on("click", function (e) {
    var list = $(this).data("list");
    if ($(this).hasClass("collapsed")) {
      $("." + list).show();
    } else {
      $("." + list).hide();
    }
    $(this).toggleClass("collapsed");
  });
  $(".clickableRow").on("click", function (evt) {
    window.open($(this).data("href"), "_blank");
  });
  $(".datetimeWF").each(function () {
    var time = $(this).text().trim();
    var timeAgo = moment(time, "YYYY/MM/DD HH:mm:ss").format(
      "YYYY/MM/DD HH:mm:ss"
    );
    var timeZone = time.substring(time.indexOf("+") + 1);
    timeAgo += " +0" + timeZone + ":00";
    $(this).text(moment(timeAgo, "YYYY/MM/DD HH:mm:ss Z").fromNow());
  });
  hightlight_restructured();
  $('a.standardButton[title][title!=""]').addClass("tooltipIcon");
});
