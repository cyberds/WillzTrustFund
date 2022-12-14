/* ===========================================================
 * pagepiling.js 1.5
 *
 * https://github.com/alvarotrigo/pagePiling.js
 * MIT licensed
 *
 * Copyright (C) 2014 alvarotrigo.com - A project by Alvaro Trigo
 *
 * ========================================================== */
(function(b,g,h,u){b.fn.pagepiling=function(G){function H(a){var d=b(".pp-section.active").index(".pp-section");a=a.index(".pp-section");return d>a?"up":"down"}function k(a,d){var c={destination:a,animated:d,activeSection:b(".pp-section.active"),anchorLink:a.data("anchor"),sectionIndex:a.index(".pp-section"),toMove:a,yMovement:H(a),leavingSection:b(".pp-section.active").index(".pp-section")+1};c.activeSection.is(a)||("undefined"===typeof c.animated&&(c.animated=!0),"undefined"!==typeof c.anchorLink&&
I(c.anchorLink,c.sectionIndex),c.destination.addClass("active").siblings().removeClass("active"),c.sectionsToMove=J(c),"down"===c.yMovement?(c.translate3d="vertical"!==options.direction?"translate3d(-100%, 0px, 0px)":"translate3d(0px, -100%, 0px)",c.scrolling="-100%",options.css3||c.sectionsToMove.each(function(a){a!=c.activeSection.index(".pp-section")&&b(this).css(p(c.scrolling))}),c.animateSection=c.activeSection):(c.translate3d="translate3d(0px, 0px, 0px)",c.scrolling="0",c.animateSection=a),
b.isFunction(options.onLeave)&&options.onLeave.call(this,c.leavingSection,c.sectionIndex+1,c.yMovement),K(c),L(c.anchorLink),M(c.anchorLink,c.sectionIndex),v=c.anchorLink,w=(new Date).getTime())}function K(a){options.css3?(x(a.animateSection,a.translate3d,a.animated),a.sectionsToMove.each(function(){x(b(this),a.translate3d,a.animated)}),setTimeout(function(){q(a)},options.scrollingSpeed)):(a.scrollOptions=p(a.scrolling),a.animated?a.animateSection.animate(a.scrollOptions,options.scrollingSpeed,options.easing,
function(){y(a);q(a)}):(a.animateSection.css(p(a.scrolling)),setTimeout(function(){y(a);q(a)},400)))}function q(a){b.isFunction(options.afterLoad)&&options.afterLoad.call(this,a.anchorLink,a.sectionIndex+1)}function J(a){return"down"===a.yMovement?b(".pp-section").map(function(d){if(d<a.destination.index(".pp-section"))return b(this)}):b(".pp-section").map(function(d){if(d>a.destination.index(".pp-section"))return b(this)})}function y(a){"up"===a.yMovement&&a.sectionsToMove.each(function(d){b(this).css(p(a.scrolling))})}
function p(a){return"vertical"===options.direction?{top:a}:{left:a}}function I(a,b){options.anchors.length?(location.hash=a,z(location.hash)):z(String(b))}function z(a){a=a.replace("#","");b("body")[0].className=b("body")[0].className.replace(/\b\s?pp-viewing-[^\s]+\b/g,"");b("body").addClass("pp-viewing-"+a)}function r(){return(new Date).getTime()-w<600+options.scrollingSpeed?!0:!1}function x(a,b,c){a.toggleClass("pp-easing",c);a.css({"-webkit-transform":b,"-moz-transform":b,"-ms-transform":b,transform:b})}
function l(a){if(!r()){a=h.event||a;a=Math.max(-1,Math.min(1,a.wheelDelta||-a.deltaY||-a.detail));var d=b(".pp-section.active"),d=A(d);0>a?m("down",d):m("up",d);return!1}}function m(a,b){if("down"==a)var c="bottom",f=e.moveSectionDown;else c="top",f=e.moveSectionUp;if(0<b.length)if(c="top"===c?!b.scrollTop():"bottom"===c?b.scrollTop()+1+b.innerHeight()>=b[0].scrollHeight:void 0,c)f();else return!0;else f()}function A(a){return scrollable=a.filter(".pp-scrollable")}function B(){return h.PointerEvent?
{down:"pointerdown",move:"pointermove",up:"pointerup"}:{down:"MSPointerDown",move:"MSPointerMove",up:"MSPointerUp"}}function C(a){var b=[];b.y="undefined"!==typeof a.pageY&&(a.pageY||a.pageX)?a.pageY:a.touches[0].pageY;b.x="undefined"!==typeof a.pageX&&(a.pageY||a.pageX)?a.pageX:a.touches[0].pageX;return b}function D(a){return"undefined"===typeof a.pointerType||"mouse"!=a.pointerType}function N(a){a=a.originalEvent;D(a)&&(a=C(a),n=a.y,touchStartX=a.x)}function O(a){var d=a.originalEvent;!E(a.target)&&
D(d)&&(a.preventDefault(),a=b(".pp-section.active"),a=A(a),r()||(d=C(d),touchEndY=d.y,touchEndX=d.x,"horizontal"===options.direction&&Math.abs(touchStartX-touchEndX)>Math.abs(n-touchEndY)?Math.abs(touchStartX-touchEndX)>f.width()/100*options.touchSensitivity&&(touchStartX>touchEndX?m("down",a):touchEndX>touchStartX&&m("up",a)):Math.abs(n-touchEndY)>f.height()/100*options.touchSensitivity&&(n>touchEndY?m("down",a):touchEndY>n&&m("up",a))))}function E(a,d){d=d||0;var c=b(a).parent();return d<options.normalScrollElementTouchThreshold&&
c.is(options.normalScrollElements)?!0:d==options.normalScrollElementTouchThreshold?!1:E(c,++d)}function P(){b("body").append('<div id="pp-nav"><ul></ul></div>');var a=b("#pp-nav");a.css("color",options.navigation.textColor);a.addClass(options.navigation.position);for(var d=0;d<b(".pp-section").length;d++){var c="";options.anchors.length&&(c=options.anchors[d]);if("undefined"!==options.navigation.tooltips){var e=options.navigation.tooltips[d];"undefined"===typeof e&&(e="")}a.find("ul").append('<li data-tooltip="'+
e+'"><a href="#'+c+'"><span></span></a></li>')}a.find("span").css("border-color",options.navigation.bulletsColor)}function M(a,d){options.navigation&&(b("#pp-nav").find(".active").removeClass("active"),a?b("#pp-nav").find('a[href="#'+a+'"]').addClass("active"):b("#pp-nav").find("li").eq(d).find("a").addClass("active"))}function L(a){options.menu&&(b(options.menu).find(".active").removeClass("active"),b(options.menu).find('[data-menuanchor="'+a+'"]').addClass("active"))}function Q(){var a=g.createElement("p"),
b,c={webkitTransform:"-webkit-transform",OTransform:"-o-transform",msTransform:"-ms-transform",MozTransform:"-moz-transform",transform:"transform"};g.body.insertBefore(a,null);for(var e in c)a.style[e]!==u&&(a.style[e]="translate3d(1px,1px,1px)",b=h.getComputedStyle(a).getPropertyValue(c[e]));g.body.removeChild(a);return b!==u&&0<b.length&&"none"!==b}var e=b.fn.pagepiling,f=b(this),v,w=0,F="ontouchstart"in h||0<navigator.msMaxTouchPoints||navigator.maxTouchPoints,n=touchStartX=touchEndY=touchEndX=
0;options=b.extend(!0,{direction:"vertical",menu:null,verticalCentered:!0,sectionsColor:[],anchors:[],scrollingSpeed:700,easing:"easeInQuart",loopBottom:!1,loopTop:!1,css3:!0,navigation:{textColor:"#000",bulletsColor:"#000",position:"right",tooltips:[]},normalScrollElements:null,normalScrollElementTouchThreshold:5,touchSensitivity:5,keyboardScrolling:!0,sectionSelector:".section",animateAnchor:!1,afterLoad:null,onLeave:null,afterRender:null},G);b.extend(b.easing,{easeInQuart:function(a,b,c,e,f){return e*
(b/=f)*b*b*b+c}});e.setScrollingSpeed=function(a){options.scrollingSpeed=a};e.setMouseWheelScrolling=function(a){a?f.get(0).addEventListener?(f.get(0).addEventListener("mousewheel",l,!1),f.get(0).addEventListener("wheel",l,!1)):f.get(0).attachEvent("onmousewheel",l):f.get(0).addEventListener?(f.get(0).removeEventListener("mousewheel",l,!1),f.get(0).removeEventListener("wheel",l,!1)):f.get(0).detachEvent("onmousewheel",l)};e.setAllowScrolling=function(a){a?(e.setMouseWheelScrolling(!0),F&&(MSPointer=
B(),f.off("touchstart "+MSPointer.down).on("touchstart "+MSPointer.down,N),f.off("touchmove "+MSPointer.move).on("touchmove "+MSPointer.move,O))):(e.setMouseWheelScrolling(!1),F&&(MSPointer=B(),f.off("touchstart "+MSPointer.down),f.off("touchmove "+MSPointer.move)))};e.setKeyboardScrolling=function(a){options.keyboardScrolling=a};e.moveSectionUp=function(){var a=b(".pp-section.active").prev(".pp-section");!a.length&&options.loopTop&&(a=b(".pp-section").last());a.length&&k(a)};e.moveSectionDown=function(){var a=
b(".pp-section.active").next(".pp-section");!a.length&&options.loopBottom&&(a=b(".pp-section").first());a.length&&k(a)};e.moveTo=function(a){var d="",d=isNaN(a)?b('[data-anchor="'+a+'"]'):b(".pp-section").eq(a-1);0<d.length&&k(d)};b(options.sectionSelector).each(function(){b(this).addClass("pp-section")});options.css3&&(options.css3=Q());b(f).css({overflow:"hidden","-ms-touch-action":"none","touch-action":"none"});e.setAllowScrolling(!0);b.isEmptyObject(options.navigation)||P();var t=b(".pp-section").length;
b(".pp-section").each(function(a){b(this).data("data-index",a);b(this).css("z-index",t);a||0!==b(".pp-section.active").length||b(this).addClass("active");"undefined"!==typeof options.anchors[a]&&b(this).attr("data-anchor",options.anchors[a]);"undefined"!==typeof options.sectionsColor[a]&&b(this).css("background-color",options.sectionsColor[a]);options.verticalCentered&&b(this).addClass("pp-table").wrapInner('<div class="pp-tableCell" style="height:100%" />');--t}).promise().done(function(){options.navigation&&
(b("#pp-nav").css("margin-top","-"+b("#pp-nav").height()/2+"px"),b("#pp-nav").find("li").eq(b(".pp-section.active").index(".pp-section")).find("a").addClass("active"));b(h).on("load",function(){var a=h.location.hash.replace("#",""),a=b('.pp-section[data-anchor="'+a+'"]');0<a.length&&k(a,options.animateAnchor)});b.isFunction(options.afterRender)&&options.afterRender.call(this)});b(h).on("hashchange",function(){var a=h.location.hash.replace("#","").split("/")[0];a.length&&a&&a!==v&&(a=isNaN(a)?b('[data-anchor="'+
a+'"]'):b(".pp-section").eq(a-1),k(a))});b(g).keydown(function(a){if(options.keyboardScrolling&&!r())switch(a.which){case 38:case 33:e.moveSectionUp();break;case 40:case 34:e.moveSectionDown();break;case 36:e.moveTo(1);break;case 35:e.moveTo(b(".pp-section").length);break;case 37:e.moveSectionUp();break;case 39:e.moveSectionDown()}});options.normalScrollElements&&(b(g).on("mouseenter",options.normalScrollElements,function(){e.setMouseWheelScrolling(!1)}),b(g).on("mouseleave",options.normalScrollElements,
function(){e.setMouseWheelScrolling(!0)}));b(g).on("click touchstart","#pp-nav a",function(a){a.preventDefault();a=b(this).parent().index();k(b(".pp-section").eq(a))});b(g).on({mouseenter:function(){var a=b(this).data("tooltip");b('<div class="pp-tooltip '+options.navigation.position+'">'+a+"</div>").hide().appendTo(b(this)).fadeIn(200)},mouseleave:function(){b(this).find(".pp-tooltip").fadeOut(200,function(){b(this).remove()})}},"#pp-nav li")}})(jQuery,document,window);

		$(document).ready(function() {

			/*
			* Plugin intialization
			*/
			$('#pagepiling').pagepiling({
				sectionsColor: ['#000000', '#ee005a', '#2C3E50', '#39C'],
				navigation: {
					'position': 'right',
					'tooltips': ['Page 1', 'Page 2', 'Page 3', 'Page 4']
				},
				afterRender: function(){
					$('#pp-nav').addClass('custom');
				},
				afterLoad: function(anchorLink, index){
					if(index>1){
						$('#pp-nav').removeClass('custom');
					}else{
						$('#pp-nav').addClass('custom');
					}
				}
			});

			if($(window).width() < 980){
				$.fn.pagepiling.setAllowScrolling(false);
			}
	
		});