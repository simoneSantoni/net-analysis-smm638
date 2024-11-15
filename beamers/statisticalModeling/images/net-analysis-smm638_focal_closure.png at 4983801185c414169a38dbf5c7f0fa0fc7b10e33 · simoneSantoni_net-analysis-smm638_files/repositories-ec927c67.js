System.register(["./chunk-vendor.js","./chunk-frameworks.js"],(function(){"use strict";var e,t,r,n,o,s,i,a,c,l,d,u,p,f,m,h,g,y,j,S,v,q,b,w,k,L;return{setters:[function(m){e=m._,t=m.t,r=m.g,n=m.Z,o=m.c,s=m.h,i=m.f,a=m.a,c=m.o,l=m.r,d=m.F,u=m.m,p=m.C,f=m.$},function(e){m=e.b,h=e.g,g=e.B,y=e.b8,j=e.a,S=e.r,v=e.n,q=e.l,b=e.M,w=e.a7,k=e.ak,L=e.c}],execute:function(){let A=class BranchFilterElement extends HTMLElement{constructor(){super(...arguments),this.abortSearch=null,this.originalSelectedItem=null}submit(e){e.preventDefault()}resetField(e){if("Escape"!==s(e))return;const t=this.field.value.trim();this.field.value="",t&&this.search()}reset(){this.field.focus(),this.field.value="",i(this.field,"input")}get activeFilter(){var e;return null!==(e=this.filters.find((e=>e.classList.contains("selected"))))&&void 0!==e?e:null}async search(){var e;this.originalSelectedItem||(this.originalSelectedItem=this.activeFilter);const t=this.field.value.trim().length>0,r=function(e){const t=e.form;if(e.value.trim()){const r=new URL(t.action,window.location.origin),n=new URLSearchParams(r.search.slice(1)),o=t.elements.namedItem("utf8");return o instanceof HTMLInputElement&&n.append("utf8",o.value),n.append("query",e.value),r.search=n.toString(),r.toString()}return t.getAttribute("data-reset-url")}(this.field);this.classList.toggle("is-search-mode",t),this.classList.add("is-loading");for(const s of this.filters)s.classList.remove("selected");t?this.allFilter.classList.add("selected"):this.originalSelectedItem&&(this.originalSelectedItem.classList.add("selected"),this.originalSelectedItem=null),null===(e=this.abortSearch)||void 0===e||e.abort();const{signal:n}=this.abortSearch=new AbortController;try{const e=await m(document,r,{signal:n});h(null,"",r),this.result.innerHTML="",this.result.appendChild(e)}catch(o){}n.aborted||this.classList.remove("is-loading")}};e([t],A.prototype,"field",void 0),e([t],A.prototype,"result",void 0),e([t],A.prototype,"allFilter",void 0),e([r],A.prototype,"filters",void 0),e([n(100)],A.prototype,"search",null),A=e([o],A);let T=class BranchFilterItemElement extends HTMLElement{get branch(){return this.getAttribute("branch")}get branches(){const e=this.closest("branch-filter").querySelectorAll("branch-filter-item");return Array.from(e).filter((e=>e.branch===this.branch))}loading(e){for(const t of this.branches)t.spinner.hidden=!e,t.destroyButton&&(t.destroyButton.hidden=e)}set mode(e){for(const t of this.branches)t.classList.toggle("Details--on","restore"===e)}async restore(e){e.preventDefault(),this.loading(!0);const t=e.target;let r;try{r=await fetch(t.action,{method:t.method,body:new FormData(t),headers:{"X-Requested-With":"XMLHttpRequest"}})}catch(n){}finally{r&&r.ok||location.reload(),this.loading(!1)}this.mode="destroy"}async destroy(e){e.preventDefault(),this.loading(!0);const t=e.target;let r;try{r=await fetch(t.action,{method:t.method,body:new FormData(t),headers:{"X-Requested-With":"XMLHttpRequest"}})}catch(n){}finally{r&&r.ok||location.reload(),this.loading(!1)}this.mode="restore"}};e([t],T.prototype,"destroyButton",void 0),e([t],T.prototype,"spinner",void 0),T=e([o],T),a(".js-new-badge-autodismiss",{constructor:HTMLFormElement,add:e=>{const t=e.closest("details");t.addEventListener("toggle",(()=>{t.hasAttribute("open")&&g(e.action,{method:e.method,body:new FormData(e)})}))}});let _=class GetRepoElement extends HTMLElement{constructor(){super(...arguments),this.shouldRefreshList=!1}showDownloadMessage(e){const t=this.findPlatform(e);t&&this.showPlatform(t)}showCodespaces(e){const t=this.findPlatform(e);t&&(this.showPlatform(t),this.loadAndUpdateContent())}refreshList(){this.shouldRefreshList&&(this.shouldRefreshList=!1,this.loadAndUpdateContent())}trackDelete(){this.shouldRefreshList=!0}hideSpinner(){this.codespaceLoadingMenu.hidden=!0}showSpinner(){this.codespaceLoadingMenu.hidden=!1}onDetailsToggle(){this.modal.hidden=!1;for(const e of this.platforms)e.hidden=!0}showPlatform(e){this.modal.hidden=!0;for(const t of this.platforms)t.getAttribute("data-platform")===e&&(t.hidden=!1)}findPlatform(e){return e.currentTarget.getAttribute("data-open-app")||y()}loadAndUpdateContent(){this.codespaceList.setAttribute("src",this.codespaceList.getAttribute("data-src"))}};e([t],_.prototype,"modal",void 0),e([t],_.prototype,"codespaceLoadingMenu",void 0),e([t],_.prototype,"codespaceList",void 0),e([r],_.prototype,"platforms",void 0),_=e([o],_),a(".repository-import",{subscribe:e=>j(e,"socket:message",(function(e){const t=e.detail.data;t.redirect_to&&(document.location.href=t.redirect_to,e.stopImmediatePropagation())}))}),c("change","input.js-repository-import-lfs-opt",(function({currentTarget:e}){const t=parseInt(e.getAttribute("data-percent-used")||""),r=e.closest(".js-repository-import-lfs-container"),n=e.getAttribute("data-used")||"";r.querySelector(".js-repository-import-lfs-warn").classList.toggle("d-none",!(t>100)),r.querySelector(".js-usage-bar").classList.toggle("exceeded",t>=100),r.querySelector(".js-usage-bar").setAttribute("aria-label",t+"%"),r.querySelector(".js-repository-import-lfs-progress").style.width=t+"%",r.querySelector("span.js-usage-text").textContent=n})),l(".js-repository-import-author-form",(async function(e,t){const r=await t.html();e.closest(".js-repository-import-author").replaceWith(r.html)})),c("click",".js-repository-import-projects-cancel-button",(function(){const e=document.querySelector(".js-repository-import-projects-cancel-form");S(e)}));let x=!1;function C(){const e=document.querySelector(".js-repo-name");i(e,"input");const t=document.querySelector('.js-owner-container [aria-checked="true"]'),r="false"!==t.getAttribute("data-org-allow-public-repos"),n=document.querySelector(".js-privacy-toggle[value=public]");E(r,n,document.querySelector(".js-privacy-toggle-label-public"),document.querySelector(".js-public-description"),document.querySelector(".js-public-restricted-by-policy-description"));const o=function(e,t){let r=!1;const n=document.querySelectorAll(".js-new-repo-internal-visibility");for(const o of n){o.hidden=!0;const e=o.querySelector(".js-privacy-toggle[value=internal]");e instanceof HTMLInputElement&&e.checked&&(r=!0)}if(e){const n=document.querySelector("#new-repo-internal-visibility-"+e);if(n){n.hidden=!1;const e=n.querySelector(".js-privacy-toggle-label-internal"),o=n.querySelector(".js-internal-description"),s=n.querySelector(".js-internal-restricted-by-policy-description"),a=n.querySelector(".js-privacy-toggle[value=internal]");if(a instanceof HTMLInputElement)return"false"===t.getAttribute("data-org-allow-internal-repos")?(a.disabled=!0,e&&e.classList.add("text-gray-light"),o&&(o.hidden=!0),s&&(s.hidden=!1)):(r&&(a.checked=!0,i(a,"change")),a.disabled=!1,e&&e.classList.remove("text-gray-light"),o&&(o.hidden=!1),s&&(s.hidden=!0)),a}}return null}(t.getAttribute("data-business-id"),t),s="false"!==t.getAttribute("data-org-allow-private-repos"),a=document.querySelector(".js-privacy-toggle[value=private]"),c=document.querySelector(".js-privacy-toggle-label-private"),l=document.querySelector(".js-private-description"),d=document.querySelector(".js-private-restricted-by-policy-description");E(s,a,c,l,d),function(){const e=document.querySelectorAll('.js-org-upgrade-link:not([hidden=""]');for(const t of e)t.hidden=!0}();const u="false"!==t.getAttribute("data-org-private-restricted-by-plan"),p=document.querySelector(".js-upgrade-private-description"),f="false"!==t.getAttribute("data-org-show-upgrade"),m=t.getAttribute("data-org-name"),h=m?document.querySelector(`a[data-upgrade-link="${m}"]`):null,g=document.querySelector(".js-ask-owner-message");s||!u?(p&&(p.hidden=!0),h&&(h.hidden=!0),g&&(g.hidden=!0)):(d&&(d.hidden=u),p&&(p.hidden=!1),h&&(h.hidden=!f),g&&(g.hidden=f));const y=t.getAttribute("data-default-new-repo-branch"),j=document.querySelector(".js-new-repo-owner-default-branch");j&&(j.textContent=y);const S=t.getAttribute("data-owner-settings-link-prefix"),v=document.querySelector(".js-new-repo-owner-settings-link-prefix");v&&(v.textContent=S);const q=t.getAttribute("data-owner-settings-url"),b=document.querySelector(".js-repo-owner-default-branch-settings-link-container"),w=document.querySelector(".js-org-repo-owner-default-branch-settings-info");if(q){const e=document.querySelector(".js-new-repo-owner-settings-link");e&&(e.href=q,b&&(b.hidden=!1)),w&&(w.hidden=!0)}else if(b&&(b.hidden=!0,w)){const e=t.hasAttribute("data-viewer-is-org-admin");w.hidden=!e}const k="true"===t.getAttribute("data-org-show-trade-controls"),L="true"===t.getAttribute("data-viewer-is-org-admin"),A="true"===t.getAttribute("data-user-show-trade-controls"),T=k&&!s,_=document.querySelector(".js-trade-controls-description"),C=document.querySelector(".js-individual-trade-controls-description");if(A||T){const e=!A&&!L&&T;d&&(d.hidden=!e),a.disabled=!0,l&&(l.hidden=!0),p&&(p.hidden=!0),h&&(h.hidden=!0),g&&(g.hidden=!0)}else _&&(_.hidden=!0),C&&(C.hidden=!0);A?(_&&(_.hidden=!0),C&&(C.hidden=!1)):T&&_&&(_.hidden=!L),function(e,t,r,n){let o=null;"private"!==e.getAttribute("data-default")||n.disabled?"internal"===e.getAttribute("data-default")&&r&&!r.disabled?o=r:t.disabled?r&&!r.disabled&&(o=r):o=t:o=n;if(!o)return;const s=t.disabled&&t.checked||n.disabled&&n.checked||r&&r.disabled&&r.checked,a=!(t.checked||r&&r.checked||n.checked);!1!==x&&!0!==s&&!0!==a||(o.checked=!0,i(o,"change"))}(t,n,o,a),function(e){for(const n of document.querySelectorAll(".js-with-permission-fields"))n.hidden=!e;for(const n of document.querySelectorAll(".js-without-permission-fields"))n.hidden=e;const t=document.querySelector(".errored"),r=document.querySelector("dl.warn");t&&(t.hidden=!e);r&&(r.hidden=!e)}("yes"===t.getAttribute("data-permission")),function(){const e=document.querySelector("#js-upgrade-container");if(!e)return;const t=document.querySelector("#js-payment-methods-form");e.firstElementChild&&t.appendChild(e.firstElementChild);const r=document.querySelector("input[name=owner]:checked").value,n=t.querySelector(`.js-upgrade[data-login="${r}"]`);n&&e.appendChild(n)}(),M();const I=document.querySelector(".js-quick-install-container");if(I){const e=I.querySelector(".js-quick-install-divider");e.hidden=!0;const t=document.querySelector("input[name=owner]:checked").parentElement;if(t){const r=t.querySelector(".js-quick-install-list-template");if(r instanceof HTMLTemplateElement){const t=I.querySelector(".js-account-apps");t.innerHTML="",t.append(r.content.cloneNode(!0)),r.children.length>0&&(e.hidden=!1)}}}}function E(e,t,r,n,o){e?(t.disabled=!1,r&&r.classList.remove("text-gray-light"),n&&(n.hidden=!1),o&&(o.hidden=!0)):(t.disabled=!0,r&&r.classList.add("text-gray-light"),n&&(n.hidden=!0),o&&(o.hidden=!1))}function M(e){const t=document.querySelector("#js-upgrade-container");if(!t)return;const r=t.querySelector(".js-billing-section"),n=t.querySelector(".js-confirm-upgrade-checkbox");let o=e?e.target:null;o||(o=document.querySelector(".js-privacy-toggle:checked")),"false"===o.value?(t.hidden=!1,r&&r.classList.remove("has-removed-contents"),n&&(n.checked=!0)):(t.hidden=!0,r&&r.classList.add("has-removed-contents"),n&&(n.checked=!1)),I()}function I(){const e=document.querySelector(".js-repo-form"),t=e.querySelector(".js-repository-owner-choice:checked"),r=e.querySelector(".js-repo-name"),n=e.querySelector(".js-repo-url"),o=e.querySelector(".js-repo-gitignore"),s=e.querySelector(".js-repo-license");let i=!n||!n.classList.contains("is-autocheck-errored");if(i=i&&!!t,i&&r&&(i=r.classList.contains("is-autocheck-successful"),"private"===document.querySelector(".js-privacy-toggle:checked").value&&(i=i&&function(){const e=document.querySelector("#js-upgrade-container");if(!e)return!0;if(e.querySelector(".js-ofac-sanction-notice"))return!1;const t=e.querySelector(".js-confirm-upgrade-checkbox");if(t instanceof HTMLInputElement&&!t.checked)return!1;const r=e.querySelector(".js-zuora-billing-info");if(r&&r.classList.contains("d-none"))return!1;return!0}())),o&&o.checked){const t=e.querySelector('input[name="repository[gitignore_template]"]:checked');i=i&&""!==t.value}if(s&&s.checked){const t=e.querySelector('input[name="repository[license_template]"]:checked');i=i&&""!==t.value}e.querySelector("button[type=submit]").disabled=!i}async function H(e){const t=e.form;t.querySelector("#release_draft").value="1",D(e,"saving");try{const r=await(await g(t.action,{method:t.method,body:new FormData(t),headers:{Accept:"application/json"}})).json();return D(e,"saved"),setTimeout(D,5e3,e,"default"),i(t,"release:saved",{release:r}),r}catch(r){throw D(e,"failed"),r}}function R(e){const t=e.closest(".js-releases-marketplace-publish-container").querySelector(".js-releases-marketplace-publish-preview");e.checked?t.classList.remove("d-none"):t.classList.add("d-none")}function D(e,t){for(const r of e.querySelectorAll(".js-save-draft-button-state"))r.hidden=r.getAttribute("data-state")!==t;e.disabled="saving"===t}function F(e){const t=document.querySelector(".js-release-target-wrapper");if(null!=t){switch(e){case"valid":t.classList.add("d-none");break;case"loading":break;default:t.classList.remove("d-none")}for(const t of document.querySelectorAll(".js-tag-status-message"))t.hidden=t.getAttribute("data-state")!==e}}a("#js-upgrade-container .js-zuora-billing-info:not(.d-none)",I),a(".page-new-repo",(function(){const e=document.querySelector("#js-upgrade-container");e&&(e.hidden=!0),C();const t=document.querySelector(".js-repo-form"),r=t.querySelector(".js-repo-url");if(r)return void r.focus();const n=t.querySelector(".js-template-repository-select");if(n)return void n.focus();const o=t.querySelector(".js-owner-select");o&&o.focus()})),c("click",".js-reponame-suggestion",(function(e){const t=document.querySelector(".js-repo-name");t.value=e.currentTarget.textContent,i(t,"input",!1)})),c("click",".js-privacy-toggle",(function(){x=!0})),c("change",".js-privacy-toggle",M),c("details-menu-selected",".js-owner-container",C,{capture:!0}),c("change","#js-upgrade-container input",I),v("#js-upgrade-container input",I),v(".js-owner-reponame .js-repo-name",(function(e){const t=document.querySelector(".js-personal");if(t){const r=document.querySelector(".js-owner-container input.js-repository-owner-is-viewer"),n=e.target,o=!(r&&r.checked&&r.defaultValue.toLowerCase()===n.value.toLowerCase());t.hidden=o;document.querySelector("#repo-name-suggestion").hidden=!o}I()})),c("auto-check-send",".js-repo-name-auto-check",(function(e){const t=e.currentTarget.form.querySelector("input[name=owner]:checked").value;e.detail.body.append("owner",t)})),c("auto-check-complete","#repository_name",(function(){I()})),v(".js-repo-url",(function(e){const t=e.target;if(!(t instanceof HTMLInputElement))return;const r=t.closest(".form-group");if(!(r instanceof HTMLDListElement))return;const n=document.querySelector(".js-insecure-url-warning"),o=document.querySelector(".js-svn-url-error"),s=document.querySelector(".js-git-url-error"),i=t.value.toLowerCase();n.hidden=!i.startsWith("http://"),o.hidden=!i.startsWith("svn://"),s.hidden=!i.startsWith("git://"),i.startsWith("svn://")||i.startsWith("git://")?(t.classList.add("is-autocheck-errored"),r.classList.add("errored")):(t.classList.remove("is-autocheck-errored"),r.classList.remove("errored")),I()})),c("change",".js-toggle-repo-init-setting",(e=>{const t=e.currentTarget;t.checked||function(e){const t=e.closest(".js-repo-init-setting-container");if(!t)return;t.querySelector(".js-repo-init-setting-unchecked-menu-option").checked=!0}(t),I()})),c("change",".js-repo-init-setting-unchecked-menu-option",(e=>{const t=e.currentTarget;t.checked&&function(e){const t=e.closest(".js-repo-init-setting-container");if(!t)return;const r=t.querySelector(".js-toggle-repo-init-setting");r.checked=!1,i(r,"change")}(t),I()})),c("change",".js-toggle-new-repo-default-branch-info",(e=>{!function(e){const t=e.closest("form"),r=t.querySelector(".js-new-repo-default-branch-info");if(!r)return;const n=t.querySelectorAll(".js-toggle-new-repo-default-branch-info:checked").length>0;r.hidden=!n}(e.currentTarget)})),c("tab-container-changed",".js-branches-tags-tabs",(async function(e){const t=e.detail.relatedTarget,r=e.currentTarget;if(!r)return;let n,o;for(const i of r.querySelectorAll("[data-controls-ref-menu-id]")){if(!(i instanceof d||i instanceof u))return;const e=i.getAttribute("data-controls-ref-menu-id"),r=t.id===e;i.hidden=!r,r?o=i:n||(n=i.input?i.input.value:"")}const s=o&&o.input;s&&(o&&void 0!==n&&(s.value=n),s.focus())})),a(".js-pulse-contribution-data",(e=>{!async function(e){const t=e.getAttribute("data-pulse-diffstat-summary-url");let r;try{t&&(r=await async function(e){return m(document,e)}(t),function(e,t){t.innerHTML="",t.appendChild(e)}(r,e))}catch(n){const t=e.querySelector(".js-blankslate-loading"),r=e.querySelector(".js-blankslate-error");t.classList.add("d-none"),r.classList.remove("d-none")}}(e)})),c("change",".js-releases-marketplace-publish-field",(function(e){R(e.currentTarget)})),a(".js-releases-marketplace-publish-field",(function(e){R(e)})),c("click",".js-save-draft",(function(e){H(e.currentTarget),e.preventDefault()})),c("click",".js-timeline-tags-expander",(function(e){e.currentTarget.closest(".js-timeline-tags").classList.remove("is-collapsed")})),c("release:saved",".js-release-form",(function(e){const t=e.detail.release,r=e.currentTarget,n=r.getAttribute("data-repo-url"),o=t.update_url||U("tag",n,t.tag_name);if(r.setAttribute("action",o),t.update_authenticity_token){r.querySelector("input[name=authenticity_token]").value=t.update_authenticity_token}const s=t.edit_url||U("edit",n,t.tag_name);h(q(),document.title,s);const i=document.querySelector("#delete_release_confirm form");if(i){const e=t.delete_url||U("tag",n,t.tag_name);if(i.setAttribute("action",e),t.delete_authenticity_token){i.querySelector("input[name=authenticity_token]").value=t.delete_authenticity_token}}const a=r.querySelector("#release_id");if(!a.value){a.value=t.id;const e=document.createElement("input");e.type="hidden",e.name="_method",e.value="put",r.appendChild(e)}})),c("click",".js-publish-release",(function(){document.querySelector("#release_draft").value="0"}));const z=new WeakMap;async function P(e){if(!e.value)return;if(e.value===z.get(e))return;F("loading"),z.set(e,e.value);const t=e.getAttribute("data-url"),r=new URL(t,window.location.origin),n=new URLSearchParams(r.search.slice(1));n.append("tag_name",e.value),r.search=n.toString();try{const t=await(await g(r.toString(),{headers:{Accept:"application/json"}})).json();"duplicate"===t.status&&parseInt(e.getAttribute("data-existing-id"))===parseInt(t.release_id)?F("valid"):(document.querySelector(".js-release-tag .js-edit-release-link").setAttribute("href",t.url),F(t.status))}catch(o){F("invalid")}}function U(e,t,r){return`${t}/releases/${e}/${r}`}function $(e){const t=e.closest("form").querySelector(".js-previewable-comment-form");if(!t)return;let r=t.getAttribute("data-base-preview-url");r||(r=String(t.getAttribute("data-preview-url")),t.setAttribute("data-base-preview-url",r));const n=e.querySelectorAll('input[name="release[tag_name]"], input[name="release[target_commitish]"]:checked'),o=new URL(r,window.location.origin),s=new URLSearchParams(o.search.slice(1));for(const i of n)i.value&&s.append(i.name,i.value);o.search=s.toString(),t.setAttribute("data-preview-url",o.toString())}a("input.js-release-tag-field",{constructor:HTMLInputElement,initialize(e){P(e),e.addEventListener("blur",(function(){P(e)}))}}),c("change",".js-release-tag",(function(e){$(e.currentTarget)})),a(".js-release-form .js-previewable-comment-form",(function(e){$(e.closest("form").querySelector(".js-release-tag"))})),c("auto-check-message-updated",".js-rename-branch-input",(function(e){!function(e){const t=e.closest(".js-rename-branch-form"),r=t.querySelectorAll(".js-rename-branch-new-name");let n=e.value;if(n!==e.defaultValue&&""!==n){const e=t.querySelector(".js-rename-branch-autocheck-message");e&&e.hasAttribute("data-normalized-name")&&(n=e.getAttribute("data-normalized-name"));for(const t of r)t.textContent=n}}(e.currentTarget)})),c("change",".js-template-repository-choice",(function(e){const t=e.target,r=t.checked&&""!==t.value,n=t.form;n.querySelector(".js-repository-auto-init-options").classList.toggle("has-removed-contents",r);const o=n.querySelectorAll(".js-template-repository-setting"),s=n.querySelectorAll(".js-template-repository-name-display");if(r){const e=t.closest(".js-template-repository-choice-container").querySelector(".js-template-repository-name"),r=t.getAttribute("data-owner"),o=n.querySelector(`.js-repository-owner-choice[value="${r}"]`);if(o instanceof HTMLInputElement)o.checked=!0,i(o,"change");else{const e=n.querySelector(".js-repository-owner-choice.js-repository-owner-is-viewer");e.checked=!0,i(e,"change")}for(const t of s)t.textContent=e.textContent}else for(const i of s)i.textContent="";for(const i of o)i.hidden=!r})),b("keydown",".js-tree-finder-field",(e=>{"Escape"===e.key&&(e.preventDefault(),history.back())}));a(".js-tree-finder",(e=>{const t=e.querySelector(".js-tree-finder-field"),r=e.querySelector(".js-tree-browser-results");if(r.childElementCount>0)return;(async e=>{if(!(e instanceof w))return;const t=e.getAttribute("data-url"),r=e.querySelector(".js-tree-browser-result-template"),{paths:n}=await(await g(t)).json();e.addLazyItems(n,(e=>{const t=r.content.cloneNode(!0).firstElementChild,n=t.querySelector(".js-tree-browser-result-anchor"),o=n.querySelector(".js-tree-browser-result-path"),s=new URL(n.href,window.location.origin);return s.pathname=`${s.pathname}/${encodeURI(e)}`,n.href=String(s),n.id="entry-"+Math.random().toString().substr(2,5),o.textContent=e,t})),e.sort()})(e);const n=new p(t,r);n.start(),e.addEventListener("fuzzy-list-will-sort",(()=>{n.stop()})),e.addEventListener("fuzzy-list-sorted",(()=>{n.start(),n.navigate()}))}));let W=null;a(".js-pjax-files",(e=>{if(!W)return void(W=window.location.pathname);const t=e.querySelector(`a[href='${W}']`);t&&setTimeout((function(){document.activeElement&&document.activeElement!==document.body||t.focus()}),200),W=window.location.pathname}));let B=null;const N=new WeakMap;function X(e){e.classList.remove("is-progress-bar");const t=e.closest(".js-upload-manifest-file-container");t.querySelector(".js-upload-progress").hidden=!0;t.querySelector(".js-upload-meter-text .js-upload-meter-filename").textContent=""}function V(e){X(e.currentTarget)}function G(e){return e.closest("form").querySelector("#release_id").value}c("file-attachment-accept",".js-upload-manifest-file",(function(e){const{attachments:t}=e.detail,r=parseInt(e.currentTarget.getAttribute("data-directory-upload-max-files")||"",10);t.length>r&&(e.preventDefault(),e.currentTarget.classList.add("is-too-many"))})),c("document:drop",".js-upload-manifest-tree-view",(async function(e){const{transfer:t}=e.detail,r=e.currentTarget,n=await f.traverse(t,!0),o=document.querySelector("#js-repo-pjax-container");o.addEventListener("pjax:success",(()=>{o.querySelector(".js-upload-manifest-file").attach(n)}),{once:!0});const s=r.getAttribute("data-drop-url");k({url:s,container:o})})),c("upload:setup",".js-upload-manifest-file",(async function(e){const{batch:t,form:r,preprocess:n}=e.detail,o=e.currentTarget;function s(){r.append("upload_manifest_id",N.get(o))}if(function(e,t){const r=e.closest(".js-upload-manifest-file-container").querySelector(".js-upload-progress");r.hidden=!1,e.classList.add("is-progress-bar");const n=r.querySelector(".js-upload-meter-text");n.querySelector(".js-upload-meter-range-start").textContent=String(t.uploaded()+1),n.querySelector(".js-upload-meter-range-end").textContent=String(t.size)}(o,t),N.get(o))return void s();if(B)return void n.push(B.then(s));const i=o.closest(".js-upload-manifest-file-container").querySelector(".js-upload-manifest-form");B=fetch(i.action,{method:i.method,body:new FormData(i),headers:{Accept:"application/json"}});const[a,c]=function(){let e;return[new Promise((t=>{e=t})),e]}();n.push(a.then(s));const l=await B;if(!l.ok)return;const d=await l.json();document.querySelector(".js-manifest-commit-form").elements.namedItem("manifest_id").value=d.upload_manifest.id,N.set(o,d.upload_manifest.id),B=null,c()})),c("upload:start",".js-upload-manifest-file",(function(e){const{attachment:t,batch:r}=e.detail,n=e.currentTarget.closest(".js-upload-manifest-file-container").querySelector(".js-upload-progress").querySelector(".js-upload-meter-text");n.querySelector(".js-upload-meter-range-start").textContent=r.uploaded()+1;n.querySelector(".js-upload-meter-filename").textContent=t.fullPath})),c("upload:complete",".js-upload-manifest-file",(function(e){const{attachment:t,batch:r}=e.detail,n=document.querySelector(".js-manifest-commit-file-template").querySelector(".js-manifest-file-entry").cloneNode(!0);n.querySelector(".js-filename").textContent=t.fullPath;const o=t.id;n.querySelector(".js-remove-manifest-file-form").elements.namedItem("file_id").value=o;const s=document.querySelector(".js-manifest-file-list");s.hidden=!1,e.currentTarget.classList.add("is-file-list");s.querySelector(".js-manifest-file-list-root").appendChild(n),r.isFinished()&&X(e.currentTarget)})),c("upload:progress",".js-upload-manifest-file",(function(e){const{batch:t}=e.detail;e.currentTarget.closest(".js-upload-manifest-file-container").querySelector(".js-upload-meter").style.width=t.percent()+"%"})),c("upload:error",".js-upload-manifest-file",V),c("upload:invalid",".js-upload-manifest-file",V),l(".js-remove-manifest-file-form",(async function(e,t){await t.html();const r=e.closest(".js-manifest-file-list-root");if(e.closest(".js-manifest-file-entry").remove(),!r.hasChildNodes()){r.closest(".js-manifest-file-list").hidden=!0;document.querySelector(".js-upload-manifest-file").classList.remove("is-file-list")}})),a(".js-manifest-ready-check",{initialize(e){!async function(e){const t=e.getAttribute("data-redirect-url");try{await L(e.getAttribute("data-poll-url")),window.location.href=t}catch(r){document.querySelector(".js-manifest-ready-check").hidden=!0,document.querySelector(".js-manifest-ready-check-failed").hidden=!1}}(e)}}),c("click",".js-release-remove-file",(function(e){const t=e.currentTarget.closest(".js-release-file");t.classList.add("delete"),t.querySelector("input.destroy").value="true"})),c("click",".js-release-undo-remove-file",(function(e){const t=e.currentTarget.closest(".js-release-file");t.classList.remove("delete"),t.querySelector("input.destroy").value=""}));let Z=null;function J(e,t){t.append("release_id",G(e));const r=Array.from(document.querySelectorAll(".js-releases-field .js-release-file.delete .id"));if(r.length){const e=r.map((e=>e.value));t.append("deletion_candidates",e.join(","))}}c("release:saved",".js-release-form",(function(e){const t=e.currentTarget;Z=null;let r=!1;for(const o of t.querySelectorAll(".js-releases-field .js-release-file"))o.classList.contains("delete")?o.remove():o.classList.contains("js-template")||(r=!0);const n=t.querySelector(".js-releases-field");n.classList.toggle("not-populated",!r),n.classList.toggle("is-populated",r)})),c("upload:setup",".js-upload-release-file",(function(e){const{form:t,preprocess:r}=e.detail,n=e.currentTarget;if(G(n))return void J(n,t);if(!Z){const e=document.querySelector(".js-save-draft");Z=H(e)}const o=J.bind(null,n,t);r.push(Z.then(o))})),c("upload:start",".js-upload-release-file",(function(e){const t=e.detail.policy;e.currentTarget.querySelector(".js-upload-meter").classList.remove("d-none");const r=t.asset.replaced_asset;if(r)for(const n of document.querySelectorAll(".js-releases-field .js-release-file .id"))Number(n.value)===r&&n.closest(".js-release-file").remove()})),c("upload:complete",".js-upload-release-file",(function(e){const{attachment:t}=e.detail,r=document.querySelector(".js-releases-field"),n=r.querySelector(".js-template").cloneNode(!0);n.classList.remove("d-none","js-template"),n.querySelector("input.id").value=t.id;const o=t.name||t.href.split("/").pop();for(const i of n.querySelectorAll(".js-release-asset-filename"))i instanceof HTMLInputElement?i.value=o:i.textContent=o;const s=`(${(t.file.size/1048576).toFixed(2)} MB)`;n.querySelector(".js-release-asset-filesize").textContent=s,r.appendChild(n),r.classList.remove("not-populated"),r.classList.add("is-populated");e.currentTarget.querySelector(".js-upload-meter").classList.add("d-none")})),c("upload:progress",".js-upload-release-file",(function(e){const{attachment:t}=e.detail;e.currentTarget.querySelector(".js-upload-meter").style.width=t.percent+"%"}))}}}));
//# sourceMappingURL=repositories-2eacfa56.js.map
