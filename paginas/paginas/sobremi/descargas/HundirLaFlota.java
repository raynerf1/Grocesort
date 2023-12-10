package HundirLaFlota;

import java.util.Scanner;

public class HundirLaFlota {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

			Scanner entrada = new Scanner(System.in);

			// PRINCIPAL

			
			//Reglas
			
			System.out.println("------------------------------------------------------");
			System.out.println("                    REGLAS                            ");
			System.out.println("------------------------------------------------------");

			System.out.println("Si quieres ver las reglas introduce [S]");
			System.out.println("Introduce cualquier otro valor en caso contrario.");
			char respuesta = entrada.next().charAt(0);
			char Respuesta = Character.toUpperCase(respuesta);
			if (Respuesta == 'S') {
				System.out.println("Se jugará sobre un tablero de 10x10 posiciones que se enumerarán:"
						+ "\nDe 0 a 9 las columnas.\nDe A a J las filas.\n"
						+ "\nSe mostrará el tablero visible al jugador y se le preguntará a qué posición (fila y columna) quiere disparar"
						+ "\nSi en esa posición hay una parte del barco, se mostrará el mensaje “Tocado”. "
						+ "\nEn el caso de que no haya ningún barco en esa posición, se mostrará el mensaje “Agua”.\r\n\n"
						+ "El usuario seguirá realizando disparos hasta que hunda todos los barcos, en cuyo caso le\r\n"
						+ "aparecerá el mensaje de “¡Has ganado! o bien, si el jugador no ha conseguido hundir todos\r\n"
						+ "los barcos en los intentos que tenía, con lo que le parecerá el mensaje de “¡Has perdido!”.”");
			} else if (Respuesta == 'N') {
			}

			// Eleccion Dificultad
			
			System.out.println("Elije la dificultad" + "\n 1. Fácil"
					+ "\n	10 barcos (5 lanchas, 3 buques, 1 acorazado y 1 portaaviones)" + "\n 	50 intentos."
					+ "\n 2. Medio" + "\n	5 barcos (2 lanchas, 1 buques, 1 acorazado y 1 portaaviones)"
					+ "\n 	30 intentos." + "\n 3. Difícil" + "\n	2 barcos (1 lancha y 1 buque)" + "\n 	10 intentos."
					+ "\n 4. Personalizado " + "\n	100 intentos.");
			
			//Variables 
			int intentos = 0;
			int lanchas = 0;
			int buques = 0;
			int acorazados = 0;
			int portaaviones = 0;
			int filas = 0;
			int columnas = 0;
			int casillasConBarcos = 0;
			int barcosTocados = 0;
			int dificultad = entrada.nextInt();
			
			// Modificacion variables segun la dificultad
			
			if (dificultad == 1) {
				intentos = 50;
				lanchas = 5;
				buques = 3;
				acorazados = 1;
				portaaviones = 1;
				filas = 9;
				columnas = 9;
				casillasConBarcos = lanchas + (buques * 3) + (acorazados * 4) + (portaaviones * 5);
			} else if (dificultad == 2) {
				intentos = 30;
				lanchas = 2;
				buques = 1;
				acorazados = 1;
				portaaviones = 1;
				filas = 9;
				columnas = 9;
				casillasConBarcos = lanchas + (buques * 3) + (acorazados * 4) + (portaaviones * 5);
			} else if (dificultad == 3) {
				intentos = 10;
				lanchas = 1;
				buques = 1;
				acorazados = 0;
				filas = 9;
				columnas = 9;
				casillasConBarcos = lanchas + (buques * 3) + (acorazados * 4) + (portaaviones * 5);
			} else if (dificultad == 4) {
				filas = 9;
				columnas = 9;
				intentos = 100;
				System.out.println(
						"Has seleccionado *PERSONALIZADO*, podrás elegir el número de lanchas, buques, acorazados y portaaviones. "
								+ "\n(Podrás seleccionar cuantas filas y columnas se generan proximamente):");
				
				// Personalizacion de la dificultad Personalizado 
				
				int comprobacion = 0;
				while (comprobacion == 0) {
					System.out.println("\nIntroduce el número de lanchas");
					lanchas = entrada.nextInt();
					if (lanchas >= 0 && lanchas <= 100) {
						comprobacion++;
					} else {
						System.out.println("El número introducido debe estar entre 0 y 100 \nPruebe otra vez \n");
					}
				}
				while (comprobacion == 1) {
					System.out.println("Introduce el número de buques");
					buques = entrada.nextInt();
					if (buques >= 0 && buques <= 30) {
						comprobacion++;
					} else {
						System.out.println("El número introducido debe estar entre 0 y 30 \nPruebe otra vez \n");
					}
				}
				while (comprobacion == 2) {
					System.out.println("Introduce el número de acorazados");
					acorazados = entrada.nextInt();
					if (acorazados >= 0 && acorazados <= 20) {
						comprobacion++;
					} else {
						System.out.println("El número introducido debe estar entre 0 y 20 \nPruebe otra vez \\n");
					}
				}
				while (comprobacion == 3) {
					System.out.println("Introduce el número de portaaviones");
					portaaviones = entrada.nextInt();
					if (portaaviones >= 0 && portaaviones <= 10) {
						comprobacion++;
					} else {
						System.out.println("El número introducido debe estar entre 0 y 10 \nPruebe otra vez \\n");
					}
				}
				casillasConBarcos = lanchas + (buques * 3) + (acorazados * 4) + (portaaviones * 5);
			}
			
			// Array del tablero
			
			int tiros = 0;
			int[][] tablero = { /* A */{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }, /* B */{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
					/* C */{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }, /* D */{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
					/* E */{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }, /* F */{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
					/* G */{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }, /* H */{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
					/* I */{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }, /* J */{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 } };
			
			// Generar barcos
			
			// Lanchas
			int lanchasGeneradas = 0;
			while (lanchasGeneradas < lanchas) {
				int LanchaL = (int) (Math.random() * (9 + 1));
				int LanchaN = (int) (Math.random() * (9 + 1));
				if (tablero[LanchaL][LanchaN] == 0) {
					tablero[LanchaL][LanchaN] = -2;
					lanchasGeneradas++;
//					Eliminar comentario para ver los barcos
//					System.out.println("Lancha");
//					System.out.println(LanchaL + " " + LanchaN);
				} else if (tablero[LanchaL][LanchaN] == -2) {
				}
			}
			// Buques
			int buquesGenerados = 0;
			while (buquesGenerados < buques) {
				int BuqueL = (int) (Math.random() * (9 + 1));
				int BuqueN = (int) (Math.random() * (7 + 1));
				if (tablero[BuqueL][BuqueN] == 0 && tablero[BuqueL][(BuqueN + 1)] == 0
						&& tablero[BuqueL][(BuqueN + 2)] == 0) {
					tablero[BuqueL][BuqueN] = -2;
					tablero[BuqueL][(BuqueN + 1)] = -2;
					tablero[BuqueL][(BuqueN + 2)] = -2;
					buquesGenerados++;
//					Eliminar comentario para ver los barcos
//					System.out.println("Buque");
//					System.out.println(BuqueL +" "+ BuqueN +"" +(BuqueN+1)+""+(BuqueN+2));
				} else if (tablero[BuqueL][BuqueN] == -2 && tablero[BuqueL][(BuqueN + 1)] == -2
						&& tablero[BuqueL][(BuqueN + 2)] == -2) {
				}
			}
			// Acorazado
			int acorazadosGenerados = 0;
			while (acorazadosGenerados < acorazados) {
				int AcorazadoL = (int) (Math.random() * (9 + 1));
				int AcorazadoN = (int) (Math.random() * (6 + 1));
				if (tablero[AcorazadoL][AcorazadoN] == 0 && tablero[AcorazadoL][(AcorazadoN + 1)] == 0
						&& tablero[AcorazadoL][(AcorazadoN + 2)] == 0 && tablero[AcorazadoL][(AcorazadoN + 3)] == 0) {
					tablero[AcorazadoL][AcorazadoN] = -2;
					tablero[AcorazadoL][(AcorazadoN + 1)] = -2;
					tablero[AcorazadoL][(AcorazadoN + 2)] = -2;
					tablero[AcorazadoL][(AcorazadoN + 3)] = -2;
					acorazadosGenerados++;
//					Eliminar comentario para ver los barcos
//					System.out.println("Acorazado");
//					System.out.println(AcorazadoL +" "+ AcorazadoN+""+(AcorazadoN+1)+""+(AcorazadoN+2)+""+(AcorazadoN+3));
				} else if (tablero[AcorazadoL][AcorazadoN] == -2 && tablero[AcorazadoL][(AcorazadoN + 1)] == -2
						&& tablero[AcorazadoL][(AcorazadoN + 2)] == -2 && tablero[AcorazadoL][(AcorazadoN + 3)] == -2) {
				}
			}
			// Portaaviones
			int portaavionesGenerados = 0;
			while (portaavionesGenerados <= (portaaviones - 1)) {
				int PortaavionesL = (int) (Math.random() * (5 + 1));
				int PortaavionesN = (int) (Math.random() * (9 + 1));
				if (tablero[PortaavionesL][PortaavionesN] == 0 && tablero[(PortaavionesL + 1)][(PortaavionesN)] == 0
						&& tablero[(PortaavionesL + 2)][PortaavionesN] == 0
						&& tablero[(PortaavionesL + 3)][PortaavionesN] == 0
						&& tablero[(PortaavionesL + 4)][PortaavionesN] == 0) {
					tablero[PortaavionesL][PortaavionesN] = -2;
					tablero[(PortaavionesL + 1)][PortaavionesN] = -2;
					tablero[(PortaavionesL + 2)][PortaavionesN] = -2;
					tablero[(PortaavionesL + 3)][PortaavionesN] = -2;
					tablero[(PortaavionesL + 4)][PortaavionesN] = -2;
					portaavionesGenerados++;
					
//					Eliminar comentario para ver los barcos
//					System.out.println("Portaaviones");
//					System.out.println(PortaavionesL+""+(PortaavionesL+1)+""+(PortaavionesL+2)+""+(PortaavionesL+3)+""+(PortaavionesL+4)+" "+PortaavionesN);
				} else if (tablero[PortaavionesL][PortaavionesN] == -2 && tablero[(PortaavionesL + 1)][PortaavionesN] == -2
						&& tablero[(PortaavionesL + 2)][PortaavionesN] == -2
						&& tablero[(PortaavionesL + 3)][PortaavionesN] == -2
						&& tablero[(PortaavionesL + 4)][PortaavionesN] == -2) {
				}
			}

			while (tiros <= intentos) {

				// Impresión tablero
				char letra = 'A';
				System.out.print("\n    0 1 2 3 4 5 6 7 8 9 ");
				for (int j = 0; j <= filas; j++) {
					System.out.print("\n " + letra + ".");
					letra++;
					for (int i = 0; i <= columnas; i++) {

						if (tablero[j][i] == 1) {
							System.out.print(" A");
						} else if (tablero[j][i] == 2) {
							System.out.print(" X");
							barcosTocados++;
						} else if (tablero[j][i] == -2) {
							System.out.print(" -");
						} else if (tablero[j][i] == 0) {
							System.out.print(" -");
						}
						;
					}
				}

				if (barcosTocados == casillasConBarcos) {
					System.out.println("\n¡FELICIDADES, HAS DERRIBADO TODOS LOS OBJETIVOS! ");
					tiros = (intentos + 1);
				} else {
				}
				// Disparos
				// Seleccion de fila
				try {
					System.out.println("\nIntroduce la fila (LETRA) que quieres seleccionar");
					char Fila = entrada.next().charAt(0);
					char fila = Character.toLowerCase(Fila);
					int filaa = 0;

					if (fila == 'a') {
						filaa = 0;
					} else if (fila == 'b') {
						filaa = 1;
					} else if (fila == 'c') {
						filaa = 2;
					} else if (fila == 'd') {
						filaa = 3;
					} else if (fila == 'e') {
						filaa = 4;
					} else if (fila == 'f') {
						filaa = 5;
					} else if (fila == 'g') {
						filaa = 6;
					} else if (fila == 'h') {
						filaa = 7;
					} else if (fila == 'i') {
						filaa = 8;
					} else if (fila == 'j') {
						filaa = 9;
					}
					// Seleccion de columna
					System.out.println("Introduce la columna (NUMERO) que quieres seleccionar ");
					int columna = entrada.nextInt();

					if (tablero[filaa][columna] == 0) {
						System.out.println("¡Fallo! Disparaste al agua.");
						tablero[filaa][columna] = 1;
						tiros++;
					} else if (tablero[filaa][columna] == -2) {
						System.out.println("¡Tocado! Has alcanzado un objetivo.");
						tablero[filaa][columna] = 2;
						tiros++;
					}

				} catch (Exception e) {
					System.err.println("!ERROR¡ Has introducido la entrada incorrectamente, vuelve a introducirlos correctamente."
							+ "			\n[Se pide introducir primero la letra y luego el número]");
				}
			}
		}
	}
