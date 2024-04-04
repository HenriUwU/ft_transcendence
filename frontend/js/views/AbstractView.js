export default class {
	constructor() {

	}

	setTitle(title) {
		document.title = title;
	}

	async getHtml() {
		return "";
	}

	async executeViewScript() {
		// Get all elements with the class 'lang-item'
		const langItems = document.querySelectorAll('.lang-item');
	
		// Loop through each lang-item element and attach a click event listener
		const langAct = document.querySelector('.active-lang').id;
		if (translations[langAct]) {
			// Loop through each element in translations[lang]
			let count = 0; // Counter for skipped elements
			for (const key in translations[langAct]) {
				if (translations[langAct].hasOwnProperty(key)) {
					// Skip the first three elements
					if (count < 3) {
						count++;
						continue;
					}
					const element = document.querySelectorAll(`.${key}`);
					if (element) {
						element.forEach(elem => {
							elem.textContent = translations[langAct][key];
						})
					}
				}
			}
		}

		langItems.forEach(langItem => {
			langItem.addEventListener('click', () => {
				const lang = langItem.getAttribute("id");
				if (translations[lang]) {
					// Loop through each element in translations[lang]
					let count = 0; // Counter for skipped elements
					for (const key in translations[lang]) {
						if (translations[lang].hasOwnProperty(key)) {
							// Skip the first three elements
							if (count < 3) {
								count++;
								continue;
							}
							const element = document.querySelectorAll(`.${key}`);
							if (element) {
								element.forEach(elem => {
									elem.textContent = translations[lang][key];
								})
							}
						}
					}
				}
			});
		});
	}
}

const translations = {
	en: {
		english: "English",
		french: "French",
		spanish: "Spanish",
		tournament_name: "TOURNAMENT NAME",
		player_stats: "PLAYER STATS",
		played_games: "PLAYED GAMES:",
		win_ratio: "WIN RATIO:",
		match_history: "MATCH HISTORY",
		victory: "VICTORY",
		defeat: "DEFEAT",
		graphic_view: "GRAPHIC VIEW",
		username: "USERNAME",
		change_username: "CHANGE USERNAME...",
		current_username: "Your current username is ",
		new_username: "New username",
		update_button: "Update",
		email_address: "EMAIL ADDRESS",
		password: "PASSWORD",
		change_password: "CHANGE PASSWORD...",
		id_old_password: "Current password",
		id_new_password1: "New password",
		id_new_password2: "Confirm new password",
		profile_pic: "PROFILE PIC",
		change_profile_pic: "CHANGE PROFILE PIC...",
		id_avatar: "Select an image:",
		friends_list: "FRIENDS LIST",
		no_friends: "No friends yet.",
		all_users: "ALL USERS",
		friend_requests: "FRIEND REQUESTS",
		no_friend_request: "No friend request.",
		id_username: "Username",
		id_password: "Password",
		sign_in_button: "Sign in",
		sign_in_with_button: "Sign in with 42",
		not_a_member: "Not a member yet?",
		sign_up_now: "Sign up now!",
		sign_up_button: "Sign up",
		sign_out_button: "Sign out"
	},
	fr: {
		english: "Anglais",
		french: "Français",
		spanish: "Espagnol",
		tournament_name: "NOM DE TOURNOI",
		player_stats: "STATS DU JOUEUR",
		played_games: "PARTIES JOUÉES:",
		win_ratio: "RATIO DE VICTOIRE:",
		match_history: "HISTORIQUE DES PARTIES",
		victory: "VICTOIRE",
		defeat: "DÉFAITE",
		graphic_view: "VUE GRAPHIQUE",
		username: "PSEUDO",
		change_username: "CHANGER LE PSEUDO...",
		current_username: "Ton pseudo actuel est ",
		new_username: "Nouveau pseudo",
		update_button: "Mettre à jour",
		email_address: "ADRESSE MAIL",
		password: "MOT DE PASSE",
		change_password: "CHANGER LE MOT DE PASSE...",
		id_old_password: "Mot de passe actuel",
		id_new_password1: "Nouveau mot de passe",
		id_new_password2: "Confirmer le nouveau mot de passe",
		profile_pic: "PHOTO DE PROFIL",
		change_profile_pic: "CHANGER LA PHOTO DE PROFIL...",
		id_avatar: "Sélectionner une image :",
		friends_list: "LISTE D'AMIS",
		no_friends: "Pas encore d'amis.",
		all_users: "TOUS LES UTILISATEURS",
		friend_requests: "REQUÊTES D'AMI",
		no_friend_request: "Aucune requête d'ami.",
		id_username: "Pseudo",
		id_password: "Mot de passe",
		sign_in_button: "Se connecter",
		sign_in_with_button: "Se connecter avec 42",
		not_a_member: "Pas encore membre ?",
		sign_up_now: "Créer un compte.",
		sign_up_button: "S'enregistrer",
		sign_out_button: "Se déconnecter"
	},
	es: {
		english: "Inglés",
		french: "Francés",
		spanish: "Español",
		tournament_name: "NOMBRE DEL TORNEO",
		player_stats: "ESTADÍSTICAS DEL JUGADOR",
		played_games: "JUEGOS JUGADOS:",
		win_ratio: "RATIO DE VICTORIA:",
		match_history: "HISTORIAL DE PARTIDOS",
		victory: "VICTORIA",
		defeat: "DERROTA",
		graphic_view: "VISTA GRÁFICA",
		username: "NOMBRE DE USUARIO",
		change_username: "CAMBIAR NOMBRE DE USUARIO...",
		current_username: "Tu nombre de usuario actual es ",
		new_username: "Nuevo nombre de usuario",
		update_button: "Actualizar",
		email_address: "CORREO ELECTRÓNICO",
		password: "CONTRASEÑA",
		change_password: "CAMBIAR CONTRASEÑA...",
		id_old_password: "Contraseña actual",
		id_new_password1: "Nueva contraseña",
		id_new_password2: "Confirmar nueva contraseña",
		profile_pic: "FOTO DE PERFIL",
		change_profile_pic: "CAMBIAR FOTO DE PERFIL...",
		id_avatar: "Seleccione una imagen:",
		friends_list: "LISTA DE AMIGOS",
		no_friends: "Aún no tienes amigos.",
		all_users: "TODOS LOS USUARIOS",
		friend_requests: "SOLICITUDES DE AMIGO",
		no_friend_request: "No hay solicitud de amistad.",
		id_username: "Nombre de usuario",
		id_password: "Contraseña",
		sign_in_button: "Iniciar sesión",
		sign_in_with_button: "Iniciar sesión con 42",
		not_a_member: "¿Todavía no eres miembro?",
		sign_up_now: "¡Regístrate ahora!",
		sign_up_button: "Registrarse",
		sign_out_button: "Cerrar sesión"
	}
};
